from OptimizationAlgorithms import random_restart_hill_climbing as rrhc
from problem2 import problem as p

pr = p.Problem()

steps = 10000
sol = rrhc.random_restart_hill_climbing(pr, steps)

print('visited = {} , expanded = {} , local minimum = {}'.format(sol.get('visited'), sol.get('expanded'),
                                                                 sol.get('local minimum')))
for node in sol.get('solution'):
    print(node.get('state'), end='         cost:')
    print(node.get('value'))
