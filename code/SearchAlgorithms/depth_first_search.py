import sys

from SearchAlgorithms.depth_limited_search import depth_limited_search


def depth_first_search(problem):
    return depth_limited_search(problem, sys.maxsize)
