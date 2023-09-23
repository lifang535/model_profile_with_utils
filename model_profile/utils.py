import pandas as pd


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
    file = ...
    with open(file) as f:
        ...  # model name, load time
    data = pd.read_csv(file, skiprows=3)
    profile['...'] = ...  # first inference and avg inference
    return profile


def load_duration(app: str, module: str, batch_size: int) -> list:
    file = ...
    durations = pd.read_csv(file, header=None)
    return durations[0].tolist()
