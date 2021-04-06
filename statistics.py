from math import ceil


def sum(values):
    sum=0
    for value in values:
        sum += value
    return sum


def mean(values):
    return sum(values)/len(values)


def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 0:
        med = values[n//2-1] + values[n//2]
        med /= 2
    else:
        med = values[ceil(n/2)-1]
    return med


