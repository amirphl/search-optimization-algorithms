from OptimizationAlgorithms import genetic as g
from problem3 import problem as p
import matplotlib.pyplot as plt

pr = p.Problem()

population_size = [10, 100, 1000]
number_of_generations = 20
mutation_rate = 0.02
tornument_size = 4
plot = False

costs = []
scores = []
for siz in population_size:
    sol = g.genetic(pr, siz, number_of_generations, mutation_rate, tornument_size, plot)
    costs.append(sol.get('cost'))
    scores.append(sol.get('score'))
    print('state = {} , score = {} , cost = {} '.format(sol.get('state'), sol.get('score'), sol.get('cost')))

fig = plt.figure()
plt.plot(population_size, costs, label='cost')
plt.plot(population_size, scores, label='fitness')
fig.suptitle('Impact of increasing population size', fontsize=12)
plt.xlabel('population size', fontsize=8)
plt.ylabel('value', fontsize=8)
fig.savefig('3_genetic_b')
plt.legend()
plt.show()
