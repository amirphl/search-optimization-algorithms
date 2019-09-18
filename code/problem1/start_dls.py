from SearchAlgorithms.data_structures import Failure, CutOff
from problem1 import problem as pr
from SearchAlgorithms import depth_limited_search as d

p = pr.Problem()
depth = 2
sol, v, e = d.depth_limited_search(p, depth)
if isinstance(sol, Failure):
    print('DLS failed. visited = {} , expanded = {} '.format(v, e))
elif isinstance(sol, CutOff):
    print('DLS CutOff. visited = {} , expanded = {} '.format(v, e))
else:
    print('DLS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')

print()
# ----------------------

depth = 3
sol, v, e = d.depth_limited_search(p, depth)
if isinstance(sol, Failure):
    print('DLS failed. visited = {} , expanded = {} '.format(v, e))
elif isinstance(sol, CutOff):
    print('DLS CutOff. visited = {} , expanded = {} '.format(v, e))
else:
    print('DLS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')

print()
# ------------------

depth = 4
sol, v, e = d.depth_limited_search(p, depth)
if isinstance(sol, Failure):
    print('DLS failed. visited = {} , expanded = {} '.format(v, e))
elif isinstance(sol, CutOff):
    print('DLS CutOff. visited = {} , expanded = {} '.format(v, e))
else:
    print('DLS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')

print()
# -----------------

depth = 10
sol, v, e = d.depth_limited_search(p, depth)
if isinstance(sol, Failure):
    print('DLS failed. visited = {} , expanded = {} '.format(v, e))
elif isinstance(sol, CutOff):
    print('DLS CutOff. visited = {} , expanded = {} '.format(v, e))
else:
    print('DLS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')
