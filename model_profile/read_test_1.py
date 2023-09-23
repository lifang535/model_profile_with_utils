# from utils import *
import pandas as pd
from pprint import pprint


def load_profile(app: str, module: str) -> dict:
    """
    :return: dict{
        'application': str,     # same as dirname
        'module': str,          # same as dirname
        'model name': str,
        'load time': str,           # cold start time (ms)
        'batch sizes': list(int),   # alternative batch sizes
        'first inference': list(float),   # first inference time (ms)
        'avg inference': list(float),     # average inference time (ms)
    }
    """
    profile = {
        'application': app,
        'module': module
    }
    file = f'{app}/{module}/{module}.csv'
    with open(file) as f:
        lines = f.readlines()
        model_info = lines[0].strip().split(': ')
        profile['model name'] = model_info[1]
        load_time_info = lines[1].strip().split(': ')
        profile['load time'] = load_time_info[1]
        ...  # model name, load time

    data = pd.read_csv(file, skiprows=3)

    # profile['application'] = app
    # profile['module'] = module
    profile['batch sizes'] = data['batch_size'].tolist()
    profile['first inference'] = data['first_inference(ms)'].tolist()
    profile['avg inference'] = data['inference_avg(ms)'].tolist()
    
    # profile['...'] = ...  # first inference and avg inference

    return profile


def load_duration(app: str, module: str, batch_size: int) -> list:
    file = f'{app}/{module}/{module}_b{batch_size}.csv'
    durations = pd.read_csv(file, header=None)
    return durations[0].tolist()


apps = ['traffic_monitoring', 'emotion_and_action_detection']
modules = ['person_and_car_recognition', 'face_recognition', 'text_extraction', 'information_summary', 
           'person_recognition', 'face_extraction', 'expression_recognition', 'posture_recognition', 'information_summary']
batch_sizes = [i for i in range(1, 33)]

# profiles = [load_profile(apps[min(i // 4, 1)], modules[i]) for i in range(9)]
profiles = {
    'traffic_monitoring': {
        'person_and_car_recognition': load_profile(apps[0], modules[0]),
        'face_recognition': load_profile(apps[0], modules[1]),
        'text_extraction': load_profile(apps[0], modules[2]),
        'information_summary': load_profile(apps[0], modules[3])
    },
    'emotion_and_action_detection': {
        'person_recognition': load_profile(apps[1], modules[4]),
        'face_extraction': load_profile(apps[1], modules[5]),
        'expression_recognition': load_profile(apps[1], modules[6]),
        'posture_recognition': load_profile(apps[1], modules[7]),
        'information_summary': load_profile(apps[1], modules[8])
    }
}

# durations = [[load_duration(apps[min(i // 4, 1)], modules[i], batch_sizes[j]) for j in range(1)] for i in range(9)]
durations = {
    'traffic_monitoring': {
        'person_and_car_recognition': [load_duration(apps[0], modules[0], batch_sizes[j]) for j in range(32)],
        'face_recognition': [load_duration(apps[0], modules[1], batch_sizes[j]) for j in range(1)],
        'text_extraction': [load_duration(apps[0], modules[2], batch_sizes[j]) for j in range(1)],
        'information_summary': [load_duration(apps[0], modules[3], batch_sizes[j]) for j in range(1)]
    },
    'emotion_and_action_detection': {
        'person_recognition': [load_duration(apps[1], modules[4], batch_sizes[j]) for j in range(32)],
        'face_extraction': [load_duration(apps[1], modules[5], batch_sizes[j]) for j in range(1)],
        'expression_recognition': [load_duration(apps[1], modules[6], batch_sizes[j]) for j in range(1)],
        'posture_recognition': [load_duration(apps[1], modules[7], batch_sizes[j]) for j in range(1)],
        'information_summary': [load_duration(apps[1], modules[8], batch_sizes[j]) for j in range(1)]
    }
}

print('-----------------------------profiles-----------------------------')
pprint(profiles)

print('-----------------------------duration-----------------------------')
pprint(durations)
