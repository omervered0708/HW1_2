import pandas


def load_data(path, features):
    """
    the function loads the data from the csv file
    :param path: the path to the csv file
    :param features: the list of relevant features
    :return: a dictionary read from the csv file containing only the keys from features
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for key, value in data.items():
        if key in features:
            new_data[key] = value
    data = new_data
    return data


def filter_by_feature(data, feature, values):
    """

    :param data: a dictionary whose keys are features from the data set
    and values are lists with the values of the features
    :param feature: a name of a categorical feature
    :param values: a set of values
    :return: 2 dictionaries: data1 which includes the records where feature received a value in the set values
    and data2  which includes the records where feature received a value that's not in values
    """
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
    """
    the function initializes dict with the keys from data and empty lists as values
    :param dict: a dictionary to initialize
    :param data: a dictionary with the keys used to initialize dict
    :return: none
    """
    for key in data.keys():
        dict[key] = []


def copy_to_dict(data, i, dict):
    """
    the function copies the ith value in each list in data to dict
    :param data: a dictionary to copy from
    :param i: index in the lists to copy
    :param dict: a dictionary to copy to
    :return: none
    """
    for key, dict_value in data.items():
        dict[key].append(dict_value[i])


def print_details(data, features, statistic_functions):
    """
    print statistical indices on 'data' according to the features in 'features' using 'statistic_functions'
    :param data: dictionary whose keys are features of the data set and values are list of records
    :param features: list of features of the data set
    :param statistic_functions: list of statistic functions from statistics.py
    :return: none
    """
    for feat in features:
        # print the name of the feature
        print(f"{feat}: ", end='')
        # print results of the statistical functions applied on the 'data[feat]' records
        print(*[func(data[feat]) for func in statistic_functions], sep=', ')
