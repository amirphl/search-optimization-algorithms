from OptimizationAlgorithms import first_choice_hill_climbing as fchc
from problem2 import problem as p

pr = p.Problem()

sol = fchc.first_choice_hill_climbing(pr)

print('visited = {} , expanded = {} , local minimum = {}'.format(sol.get('visited'), sol.get('expanded'),
                                                                 sol.get('local minimum')))
for node in sol.get('solution'):
    print(node.get('state'), end='         cost:')
    print(node.get('value'))
