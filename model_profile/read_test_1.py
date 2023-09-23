# from utils import *

# profile = load_profile('traffic_monitoring/', 'person_recognition_32/yolos-tiny.csv')

# print(profile)

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

# app_1 = 'traffic_monitoring'
# app_2 = 'emotion_and_action_detection'

# # app: traffic_monitoring
# profile_1 = load_profile(app_1, 'person_and_car_recognition')
# profile_2 = load_profile(app_1, 'face_recognition')
# profile_3 = load_profile(app_1, 'text_extraction')
# profile_4 = load_profile(app_1, 'information_summary')

# # app: emotion_and_action_detection
# profile_5 = load_profile(app_2, 'person_recognition')
# profile_6 = load_profile(app_2, 'face_extraction')
# profile_7 = load_profile(app_2, 'expression_recognition')
# profile_8 = load_profile(app_2, 'posture_recognition')
# profile_9 = load_profile(app_2, 'information_summary')

# pprint(f"app: {app_1}")
# pprint(profile_1)
# pprint(profile_2)
# pprint(profile_3)
# pprint(profile_4)
# pprint(f"app: {app_2}")
# pprint(profile_5)
# pprint(profile_6)
# pprint(profile_7)
# pprint(profile_8)
# pprint(profile_9)

# # batch_size: 1
# duration_1_b1 = load_duration(app_1, 'person_and_car_recognition', 1)
# duration_2_b1 = load_duration(app_1, 'face_recognition', 1)
# duration_3_b1 = load_duration(app_1, 'text_extraction', 1)
# duration_4_b1 = load_duration(app_1, 'information_summary', 1)
# duration_5_b1 = load_duration(app_2, 'person_recognition', 1)
# duration_6_b1 = load_duration(app_2, 'face_extraction', 1)
# duration_7_b1 = load_duration(app_2, 'expression_recognition', 1)
# duration_8_b1 = load_duration(app_2, 'posture_recognition', 1)
# duration_9_b1 = load_duration(app_2, 'information_summary', 1)

# pprint(f"batch_size: 1")
# pprint(duration_1_b1)
# pprint(duration_2_b1)
# pprint(duration_3_b1)
# pprint(duration_4_b1)
# pprint(duration_5_b1)
# pprint(duration_6_b1)
# pprint(duration_7_b1)
# pprint(duration_8_b1)
# pprint(duration_9_b1)

apps = ['traffic_monitoring', 'emotion_and_action_detection']
modules = ['person_and_car_recognition', 'face_recognition', 'text_extraction', 'information_summary', 
           'person_recognition', 'face_extraction', 'expression_recognition', 'posture_recognition', 'information_summary']
batch_sizes = [i for i in range(1, 33)]

# profile_1_s = [load_profile(apps[0], modules[i]) for i in range(4)]
# profile_2_s = [load_profile(apps[1], modules[i]) for i in range(4, 9)]

profiles = [load_profile(apps[min(i // 4, 1)], modules[i]) for i in range(9)]

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



