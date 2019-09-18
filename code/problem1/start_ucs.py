from SearchAlgorithms.data_structures import Failure
from problem1 import problem as pr
from SearchAlgorithms import uniform_cost_search as u

p = pr.Problem()

sol = u.uniform_cost_search(p)
if isinstance(sol, Failure):
    print('UCS failed.')
else:
    print('UCS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')
