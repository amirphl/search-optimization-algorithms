from OptimizationAlgorithms import hill_climbing as hc
from problem2 import problem as p

pr = p.Problem()

sol = hc.hill_climbing(pr)

print('visited = {} , expanded = {} , local minimum = {}'.format(sol.get('visited'), sol.get('expanded'),
                                                                 sol.get('local minimum')))
for node in sol.get('solution'):
    print(node.get('state'), end='         cost:')
    print(node.get('value'))
