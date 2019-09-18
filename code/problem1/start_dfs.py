from SearchAlgorithms.data_structures import Failure
from problem1 import problem as pr
from SearchAlgorithms import depth_first_search as de

p = pr.Problem()

sol, v, e = de.depth_first_search(p)
if isinstance(sol, Failure):
    print('DLS failed. visited = {} , expanded = {} '.format(v, e))
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
