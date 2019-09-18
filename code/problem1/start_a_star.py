from SearchAlgorithms.data_structures import Failure
from problem1 import problem as pr
from SearchAlgorithms import a_star as a

p = pr.Problem()

sol = a.a_star(p)
if isinstance(sol, Failure):
    print('A* failed.')
else:
    print('A*:')
    print(
        "visited = {} , expanded = {} , max_memory = {} , path_cost = {}".format(sol.visited, sol.expanded,
                                                                                 sol.max_memory,
                                                                                 sol.path_cost))
    print('Path:')
    for node in sol.best_path:
        print(node.state, end='')
        print(' , ', end=' ')
