from random import randint
from math import exp

import sys

import numpy as np

sample_size = 100


def simulated_annealing(problem):
    expanded = 0
    visited = 1
    current = problem.initialState
    solution = [current]
    for t in range(1, sys.maxsize):
        u = schedule(t)
        if u == 0:
            return {'expanded': expanded, 'visited': visited, 'solution': solution,
                    'local minimum': current.get('value')}
        next_one, num = problem.random_successor_v2(current)
        visited += num
        expanded += 1
        delta = next_one.get('value') - current.get('value')
        if delta <= 0:
            current = next_one
            solution.append(next_one)
        else:
            sample = np.random.choice(2, sample_size, p=[1 - exp(-1.0 * delta / u), exp(-1.0 * delta / u)])
            r = randint(0, sample_size - 1)
            x = sample[r]
            if x == 1:
                current = next_one
                solution.append(next_one)
    return {'expanded': expanded, 'visited': visited, 'solution': solution, 'local minimum': current.get('value')}


def schedule(t):
    try:
        u = 1.0 / (1.1 ** t)
        return u
    except OverflowError:
        return 0
