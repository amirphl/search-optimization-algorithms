from SearchAlgorithms.data_structures import Failure
from problem1 import problem as pr
from SearchAlgorithms import breadth_first_search as b

p = pr.Problem()

sol = b.breadth_first_search(p)
if isinstance(sol, Failure):
    print('BFS failed.')
else:
    print('BFS:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')
