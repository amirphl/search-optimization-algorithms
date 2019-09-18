from OptimizationAlgorithms import simulated_annealing as sa
from problem2 import problem as p

pr = p.Problem()

sol = sa.simulated_annealing(pr)

print('visited = {} , expanded = {} , local minimum = {}'.format(sol.get('visited'), sol.get('expanded'),
                                                                 sol.get('local minimum')))
for node in sol.get('solution'):
    print(node.get('state'), end='         cost:')
    print(node.get('value'))
