from SearchAlgorithms.data_structures import Failure
from problem1 import problem as pr
from SearchAlgorithms import greedy_best_first_search as g

p = pr.Problem()

sol = g.greedy_best_first_search(p)
if isinstance(sol, Failure):
    print('gbfs failed.')
else:
    print('gbfs:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')
