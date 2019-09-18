# source : https://stackoverflow.com/questions/4113307/pythonic-way-to-select-list-elements-with-different-probability
# Thanks to Christian

import random
import bisect
import collections


def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0
    for w in weights:
        cumsum += w
        result.append(cumsum / total)
    return result


def choice(population, weights):
    assert len(population) == len(weights)
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return population[idx]


def select(population, weights):
    counts = collections.defaultdict(int)
    for i in range(10000):
        counts[choice(population, weights)] += 1
    x = None
    y = None
    for c in counts:
        if x is None:
            x = c
            y = counts.get(x)
            continue
        if counts.get(c) < y:
            x = c
            y = counts.get(x)
    return x, y
