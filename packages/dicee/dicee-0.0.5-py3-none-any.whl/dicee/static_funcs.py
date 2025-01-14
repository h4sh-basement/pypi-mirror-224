import numpy as np
import torch
import datetime
from typing import Tuple, List
from .models import CMult, Pyke, DistMult, KeciBase, Keci, TransE, \
    ComplEx, AConEx, AConvO, AConvQ, ConvQ, ConvO, ConEx, QMult, OMult, Shallom
from .models.pykeen_models import PykeenKGE
import time
import pandas as pd
import json
import glob
import functools
import os
import psutil
from .models.base_model import BaseKGE
import pickle

def timeit(func):
    @functools.wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Took {total_time:.4f} secs '
            f'| Current Memory Usage {psutil.Process(os.getpid()).memory_info().rss / 1000000: .5} in MB')
        return result

    return timeit_wrapper


def save_pickle(*, data: object, file_path=str):
    pickle.dump(data, open(file_path, "wb"))


def load_pickle(file_path=str):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


# @TODO: Could these funcs can be merged?
def select_model(args: dict, is_continual_training: bool = None, storage_path: str = None):
    isinstance(args, dict)
    assert len(args) > 0
    assert isinstance(is_continual_training, bool)
    assert isinstance(storage_path, str)
    if is_continual_training:
        print('Loading pre-trained model...')
        model, _ = intialize_model(args)
        try:
            weights = torch.load(storage_path + '/model.pt', torch.device('cpu'))
            model.load_state_dict(weights)
            for parameter in model.parameters():
                parameter.requires_grad = True
            model.train()
        except FileNotFoundError:
            print(f"{storage_path}/model.pt is not found. The model will be trained with random weights")
        return model, _
    else:
        return intialize_model(args)


def load_model(path_of_experiment_folder, model_name='model.pt') -> Tuple[object, dict, dict]:
    """ Load weights and initialize pytorch module from namespace arguments"""
    print(f'Loading model {model_name}...', end=' ')
    start_time = time.time()
    # (1) Load weights..
    weights = torch.load(path_of_experiment_folder + f'/{model_name}', torch.device('cpu'))
    # (2) Loading input configuration..
    configs = load_json(path_of_experiment_folder + '/configuration.json')
    # (3) Loading the report of a training process.
    report = load_json(path_of_experiment_folder + '/report.json')
    configs["num_entities"] = report["num_entities"]
    configs["num_relations"] = report["num_relations"]
    print(f'Done! It took {time.time() - start_time:.3f}')
    # (4) Select the model
    model, _ = intialize_model(configs)
    # (5) Put (1) into (4)
    model.load_state_dict(weights)
    # (6) Set it into eval model.
    for parameter in model.parameters():
        parameter.requires_grad = False
    model.eval()
    start_time = time.time()
    print('Loading entity and relation indexes...', end=' ')
    with open(path_of_experiment_folder + '/entity_to_idx.p', 'rb') as f:
        entity_to_idx = pickle.load(f)
    with open(path_of_experiment_folder + '/relation_to_idx.p', 'rb') as f:
        relation_to_idx = pickle.load(f)
    assert isinstance(entity_to_idx, dict)
    assert isinstance(relation_to_idx, dict)
    print(f'Done! It took {time.time() - start_time:.4f}')
    return model, entity_to_idx, relation_to_idx


def load_model_ensemble(path_of_experiment_folder: str) -> Tuple[BaseKGE, pd.DataFrame, pd.DataFrame]:
    """ Construct Ensemble Of weights and initialize pytorch module from namespace arguments

    (1) Detect models under given path
    (2) Accumulate parameters of detected models
    (3) Normalize parameters
    (4) Insert (3) into model.
    """
    print('Constructing Ensemble of ', end=' ')
    start_time = time.time()
    # (1) Detect models under given path.
    paths_for_loading = glob.glob(path_of_experiment_folder + '/model*')
    print(f'{len(paths_for_loading)} models...')
    assert len(paths_for_loading) > 0
    num_of_models = len(paths_for_loading)
    weights = None
    # (2) Accumulate parameters of detected models.
    while len(paths_for_loading):
        p = paths_for_loading.pop()
        print(f'Model: {p}...')
        if weights is None:
            weights = torch.load(p, torch.device('cpu'))
        else:
            five_weights = torch.load(p, torch.device('cpu'))
            # (2.1) Accumulate model parameters
            for k, _ in weights.items():
                if 'weight' in k:
                    weights[k] = (weights[k] + five_weights[k])
    # (3) Normalize parameters.
    for k, _ in weights.items():
        if 'weight' in k:
            weights[k] /= num_of_models
    # (4) Insert (3) into model
    # (4.1) Load report and configuration to initialize model.
    configs = load_json(path_of_experiment_folder + '/configuration.json')
    report = load_json(path_of_experiment_folder + '/report.json')
    configs["num_entities"] = report["num_entities"]
    configs["num_relations"] = report["num_relations"]
    print(f'Done! It took {time.time() - start_time:.2f} seconds.')
    # (4.2) Select the model
    model, _ = intialize_model(configs)
    # (4.3) Put (3) into their places
    model.load_state_dict(weights, strict=True)
    # (6) Set it into eval model.
    print('Setting Eval mode & requires_grad params to False')
    for parameter in model.parameters():
        parameter.requires_grad = False
    model.eval()
    start_time = time.time()
    print('Loading entity and relation indexes...', end=' ')
    with open(path_of_experiment_folder + '/entity_to_idx.p', 'rb') as f:
        entity_to_idx = pickle.load(f)
    with open(path_of_experiment_folder + '/relation_to_idx.p', 'rb') as f:
        relation_to_idx = pickle.load(f)
    assert isinstance(entity_to_idx, dict)
    assert isinstance(relation_to_idx, dict)
    print(f'Done! It took {time.time() - start_time:.4f}')
    return model, entity_to_idx, relation_to_idx


def save_numpy_ndarray(*, data: np.ndarray, file_path: str):
    n, d = data.shape
    assert n > 0
    assert d == 3
    with open(file_path, 'wb') as f:
        np.save(f, data)


def numpy_data_type_changer(train_set: np.ndarray, num: int) -> np.ndarray:
    """
    Detect most efficient data type for a given triples
    :param train_set:
    :param num:
    :return:
    """
    assert isinstance(num, int)
    if np.iinfo(np.int8).max > num:
        # print(f'Setting int8,\t {np.iinfo(np.int8).max}')
        train_set = train_set.astype(np.int8)
    elif np.iinfo(np.int16).max > num:
        # print(f'Setting int16,\t {np.iinfo(np.int16).max}')
        train_set = train_set.astype(np.int16)
    elif np.iinfo(np.int32).max > num:
        # print(f'Setting int32,\t {np.iinfo(np.int32).max}')
        train_set = train_set.astype(np.int32)
    else:
        raise TypeError('Int64?')
    return train_set


def save_checkpoint_model(model, path: str) -> None:
    """ Store Pytorch model into disk"""
    if isinstance(model, BaseKGE):
        try:
            torch.save(model.state_dict(), path)
        except ReferenceError as e:
            print(e)
            print(model.name)
            print('Could not save the model correctly')
    else:
        torch.save(model.model.state_dict(), path)


def store(trainer,
          trained_model, model_name: str = 'model', full_storage_path: str = None, save_embeddings_as_csv=False) -> None:
    """
    Store trained_model model and save embeddings into csv file.
    :param trainer: an instance of trainer class
    :param dataset: an instance of KG see core.knowledge_graph.
    :param full_storage_path: path to save parameters.
    :param model_name: string representation of the name of the model.
    :param trained_model: an instance of BaseKGE see core.models.base_model .
    :param save_embeddings_as_csv: for easy access of embeddings.
    :return:
    """
    assert full_storage_path is not None
    assert isinstance(model_name, str)
    assert len(model_name) > 1

    # (1) Save pytorch model in trained_model .
    save_checkpoint_model(model=trained_model, path=full_storage_path + f'/{model_name}.pt')
    if save_embeddings_as_csv:
        entity_emb, relation_ebm = trained_model.get_embeddings()
        entity_to_idx = pickle.load(open(full_storage_path + '/entity_to_idx.p', 'rb'))
        entity_str = entity_to_idx.keys()
        # Ensure that the ordering is correct.
        assert list(range(0, len(entity_str))) == list(entity_to_idx.values())
        save_embeddings(entity_emb.numpy(), indexes=entity_str,
                        path=full_storage_path + '/' + trained_model.name + '_entity_embeddings.csv')
        del entity_to_idx, entity_str, entity_emb
        if relation_ebm is not None:
            relation_to_idx = pickle.load(open(full_storage_path + '/relation_to_idx.p', 'rb'))
            relations_str = relation_to_idx.keys()

            save_embeddings(relation_ebm.numpy(), indexes=relations_str,
                            path=full_storage_path + '/' + trained_model.name + '_relation_embeddings.csv')
            del relation_ebm, relations_str, relation_to_idx
        else:
            pass


def add_noisy_triples(train_set: pd.DataFrame, add_noise_rate: float) -> pd.DataFrame:
    """
    Add randomly constructed triples
    :param train_set:
    :param add_noise_rate:
    :return:
    """
    num_triples = len(train_set)
    num_noisy_triples = int(num_triples * add_noise_rate)
    print(f'[4 / 14] Generating {num_noisy_triples} noisy triples for training data...')

    list_of_entities = pd.unique(train_set[['subject', 'object']].values.ravel())

    train_set = pd.concat([train_set,
                           # Noisy triples
                           pd.DataFrame(
                               {'subject': np.random.choice(list_of_entities, num_noisy_triples),
                                'relation': np.random.choice(
                                    pd.unique(train_set[['relation']].values.ravel()),
                                    num_noisy_triples),
                                'object': np.random.choice(list_of_entities, num_noisy_triples)}
                           )
                           ], ignore_index=True)

    del list_of_entities

    assert num_triples + num_noisy_triples == len(train_set)
    return train_set


def read_or_load_kg(args, cls):
    print('*** Read or Load Knowledge Graph  ***')
    start_time = time.time()
    kg = cls(data_dir=args.path_dataset_folder,
             add_noise_rate=args.add_noise_rate,
             sparql_endpoint=args.sparql_endpoint,
             path_single_kg=args.path_single_kg,
             add_reciprical=args.apply_reciprical_or_noise,
             eval_model=args.eval_model,
             read_only_few=args.read_only_few,
             sample_triples_ratio=args.sample_triples_ratio,
             path_for_serialization=args.full_storage_path,
             path_for_deserialization=args.path_experiment_folder if hasattr(args, 'path_experiment_folder') else None,
             backend=args.backend)
    print(f'Preprocessing took: {time.time() - start_time:.3f} seconds')
    # (2) Share some info about data for easy access.
    print(kg.description_of_input)
    return kg


def intialize_model(args: dict) -> Tuple[object, str]:
    # @TODO: Apply construct_krone as callback? or use KronE_QMult as a prefix.
    # @TODO: Remove form_of_labelling
    model_name = args['model']
    if "pykeen" in model_name.lower():
        model = PykeenKGE(args=args)
        form_of_labelling = "EntityPrediction"
    elif model_name == 'Shallom':
        model = Shallom(args=args)
        form_of_labelling = 'RelationPrediction'
    elif model_name == 'ConEx':
        model = ConEx(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'AConEx':
        model = AConEx(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'QMult':
        model = QMult(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'OMult':
        model = OMult(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'ConvQ':
        model = ConvQ(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'AConvQ':
        model = AConvQ(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'ConvO':
        model = ConvO(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'AConvO':
        model = AConvO(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'ComplEx':
        model = ComplEx(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'DistMult':
        model = DistMult(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'TransE':
        model = TransE(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'Pyke':
        model = Pyke(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'Keci':
        model = Keci(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'KeciBase':
        model = KeciBase(args=args)
        form_of_labelling = 'EntityPrediction'
    elif model_name == 'CMult':
        model = CMult(args=args)
        form_of_labelling = 'EntityPrediction'
    else:
        raise ValueError(f"--model_name: {model_name} is not found.")
    return model, form_of_labelling


def load_json(p: str) -> dict:
    assert os.path.isfile(p)
    with open(p, 'r') as r:
        args = json.load(r)
    return args


def save_embeddings(embeddings: np.ndarray, indexes, path: str) -> None:
    """
    Save it as CSV if memory allows.
    :param embeddings:
    :param indexes:
    :param path:
    :return:
    """
    # @TODO: Do we need it ?!
    try:
        df = pd.DataFrame(embeddings, index=indexes)
        df.to_csv(path)
    except KeyError or AttributeError as e:
        print('Exception occurred at saving entity embeddings. Computation will continue')
        print(e)
    del df


def random_prediction(pre_trained_kge):
    head_entity: List[str]
    relation: List[str]
    tail_entity: List[str]
    head_entity = pre_trained_kge.sample_entity(1)
    relation = pre_trained_kge.sample_relation(1)
    tail_entity = pre_trained_kge.sample_entity(1)
    triple_score = pre_trained_kge.triple_score(h=head_entity,
                                                r=relation,
                                                t=tail_entity)
    return f'( {head_entity[0]},{relation[0]}, {tail_entity[0]} )', pd.DataFrame({'Score': triple_score})


def deploy_triple_prediction(pre_trained_kge, str_subject, str_predicate, str_object):
    triple_score = pre_trained_kge.triple_score(h=[str_subject],
                                                r=[str_predicate],
                                                t=[str_object])
    return f'( {str_subject}, {str_predicate}, {str_object} )', pd.DataFrame({'Score': triple_score})


def deploy_tail_entity_prediction(pre_trained_kge, str_subject, str_predicate, top_k):
    if pre_trained_kge.model.name == 'Shallom':
        print('Tail entity prediction is not available for Shallom')
        raise NotImplementedError
    scores, entity = pre_trained_kge.predict_topk(h=[str_subject], r=[str_predicate], topk=top_k)
    return f'(  {str_subject},  {str_predicate}, ? )', pd.DataFrame({'Entity': entity, 'Score': scores})


def deploy_head_entity_prediction(pre_trained_kge, str_object, str_predicate, top_k):
    if pre_trained_kge.model.name == 'Shallom':
        print('Head entity prediction is not available for Shallom')
        raise NotImplementedError

    scores, entity = pre_trained_kge.predict_topk(t=[str_object], r=[str_predicate], topk=top_k)
    return f'(  ?,  {str_predicate}, {str_object} )', pd.DataFrame({'Entity': entity, 'Score': scores})


def deploy_relation_prediction(pre_trained_kge, str_subject, str_object, top_k):
    scores, relations = pre_trained_kge.predict_topk(h=[str_subject], t=[str_object], topk=top_k)
    return f'(  {str_subject}, ?, {str_object} )', pd.DataFrame({'Relations': relations, 'Score': scores})


def semi_supervised_split(train_set: np.ndarray, train_split_ratio=None, calibration_split_ratio=None):
    """
    Split input triples into three splits
    1. split corresponds to the first 10% of the input
    2. split corresponds to the second 10% of the input
    3. split corresponds to the remaining data.
    """
    # Divide train_set into
    n, d = train_set.shape
    assert d == 3
    # (1) Select X % of the first triples for the training.
    train = train_set[: int(n * train_split_ratio)]
    # (2) Select remaining first Y % of the triples for the calibration.
    calibration = train_set[len(train):len(train) + int(n * calibration_split_ratio)]
    # (3) Consider remaining triples as unlabelled.
    unlabelled = train_set[-len(train) - len(calibration):]
    print(f'Shapes:\tTrain{train.shape}\tCalib:{calibration.shape}\tUnlabelled:{unlabelled.shape}')
    return train, calibration, unlabelled


def p_value(non_conf_scores, act_score):
    if len(act_score.shape) < 2:
        act_score = act_score.unsqueeze(-1)

    # return (torch.sum(non_conf_scores >= act_score) + 1) / (len(non_conf_scores) + 1)
    return (torch.sum(non_conf_scores >= act_score, dim=-1) + 1) / (len(non_conf_scores) + 1)


def norm_p_value(p_values, variant):
    if len(p_values.shape) < 2:
        p_values = p_values.unsqueeze(0)

    if variant == 0:
        norm_p_values = p_values / (torch.max(p_values, dim=-1).values.unsqueeze(-1))
    else:
        norm_p_values = p_values.scatter_(1, torch.max(p_values, dim=-1).indices.unsqueeze(-1),
                                          torch.ones_like(p_values))
    return norm_p_values


@timeit
def vocab_to_parquet(vocab_to_idx, name, path_for_serialization, print_into):
    # @TODO: This function should take any DASK/Pandas DataFrame or Series.
    print(print_into)
    vocab_to_idx.to_parquet(path_for_serialization + f'/{name}', compression='gzip', engine='pyarrow')
    print('Done !\n')

def create_experiment_folder(folder_name='Experiments'):
    directory = os.getcwd() + "/" + folder_name + "/"
    # folder_name = str(datetime.datetime.now())
    folder_name = str(datetime.datetime.now()).replace(":", "-")
    # path_of_folder = directory + folder_name
    path_of_folder = os.path.join(directory, folder_name)
    os.makedirs(path_of_folder)
    return path_of_folder


def continual_training_setup_executor(executor) -> None:
    """
    storage_path:str A path leading to a parent directory, where a subdirectory containing KGE related data

    full_storage_path:str A path leading to a subdirectory containing KGE related data

    """
    if executor.is_continual_training:
        # (4.1) If it is continual, then store new models on previous path.
        executor.storage_path = executor.args.full_storage_path
    else:
        # Create a single directory containing KGE and all related data
        if executor.args.path_to_store_single_run:
            os.makedirs(executor.args.path_to_store_single_run, exist_ok=False)
            executor.args.full_storage_path=executor.args.path_to_store_single_run
        else:
            # Create a parent and subdirectory.
            executor.args.full_storage_path = create_experiment_folder(folder_name=executor.args.storage_path)
        executor.storage_path = executor.args.full_storage_path
        with open(executor.args.full_storage_path + '/configuration.json', 'w') as file_descriptor:
            temp = vars(executor.args)
            json.dump(temp, file_descriptor, indent=3)


def exponential_function(x: np.ndarray, lam: float, ascending_order=True) -> torch.FloatTensor:
    # A sequence in exponentially decreasing order
    result = np.exp(-lam * x) / np.sum(np.exp(-lam * x))
    assert 0.999 < sum(result) < 1.0001
    result = np.flip(result) if ascending_order else result
    return torch.tensor(result.tolist())


@timeit
def load_numpy(path) -> np.ndarray:
    print('Loading indexed training data...', end='')
    with open(path, 'rb') as f:
        data = np.load(f)
    return data
