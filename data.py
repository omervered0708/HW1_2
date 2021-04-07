import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for key, value in data.items():
        if key in features:
            new_data[key] = value
    data = new_data
    return data


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    init_dict(data1, data)
    init_dict(data2, data)
    for i, value in enumerate(data[feature]):
        if value in values:
            copy_to_dict(data, i, data1)
        else:
            copy_to_dict(data, i, data2)
    return data1, data2


def init_dict(dict, data):
    for key in data.keys():
        dict[key] = []


def copy_to_dict(data, i, dict):
    for key, dict_value in data.items():
        dict[key].append(dict_value[i])



