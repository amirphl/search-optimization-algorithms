from OptimizationAlgorithms import genetic as g
from problem2 import problem as p

pr = p.Problem()

population_size = 100
number_of_generations = 20
mutation_rate = 0.02
tornument_size = 4
sol = g.genetic(pr, population_size, number_of_generations, mutation_rate, tornument_size)

print('state = {} , score = {} , cost = {} '.format(sol.get('state'), sol.get('score'), sol.get('cost')))
