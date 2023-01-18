import numpy as np


def getMinimum(input_double):
    res = input_double[0]
    for i in input_double:
        if res > i:
            res = i
    return res


def getMaximum(input_double):
    res = input_double[0]
    for i in input_double:
        if res < i:
            res = i
    return res


# enter amount_of_period  percent of filtered data
# 1                       68
# 2                       95
# 3                       99.7

def predictionLimits(data, amount_of_period=1):
    res = []
    mean_val = np.mean(data)
    st_dev = np.std(data)
    if amount_of_period < 1:
        amount_of_period = 1
    res.append(mean_val - amount_of_period * st_dev)
    res.append((mean_val + amount_of_period * st_dev))
    return res
