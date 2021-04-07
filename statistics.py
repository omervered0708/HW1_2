from math import ceil


def sum(values):
    """
    return the sum of values
    :param values: list of numeric values
    :return: the sum of values
    """
    sum = 0
    for value in values:
        sum += value
    return sum


def mean(values):
    """
    return the mean of values
    :param values: list of numeric values
    :return: the mean of values
    """
    return sum(values)/len(values)


def median(values):
    """
    return the median of values
    :param values: list of numeric values
    :return: median of values
    """
    values.sort()
    n = len(values)
    if n % 2 == 0:
        med = values[(n//2)-1] + values[n//2]
        med /= 2
    else:
        med = values[ceil(n/2)-1]
    return med


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    print statistical indices about data which represents population.
    the statistical indices are measured on the feature target gathering records by the following rules:
    if is_above is True - gather records in which treatment's values are greater then or equal to "threshold"
    :param feature_description: string to describe the name of the set
    :param data: dictionary which its keys are features from the data set and values are lists of the features' values
    :param treatment: name of a feature from the data set
    :param target: name of a feature from the data set
    :param threshold: threshold value for feature treatment
    :param is_above: indicator which receives True or False
    :param statistic_functions: list which contains the statistics methods from statistics.py
    :return: none
    """
    # create a list containing only relevant records
    # create a list of pairs (tuples) of corresponding values from 'data'
    joint_list = zip(data[treatment], data[target])
    # filter elements which do not satisfy is_above threshold (by the 'treatment' value),
    # then reduce the list to only 'target' values
    records = [[elem[1]] for elem in list(filter(lambda elem: is_above == (elem[0] > threshold), joint_list))]

    # print feature description and target feature
    print(f"{feature_description}:\n{target.__name__}: ", end='')
    # print statistics
    print(*[[func(records)] for func in statistic_functions], sep=', ', end='\n')
