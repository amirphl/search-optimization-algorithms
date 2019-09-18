from OptimizationAlgorithms import genetic as g
from problem2 import problem as p
import matplotlib.pyplot as plt

pr = p.Problem()

population_size = 100
number_of_generations = 20
mutation_rate = [0.02, 0.05, 0.1, 0.3, 0.5, 0.9, 1]
tornument_size = 4
plot = False

costs = []
scores = []
for rate in mutation_rate:
    sol = g.genetic(pr, population_size, number_of_generations, rate, tornument_size, plot)
    costs.append(sol.get('cost'))
    scores.append(sol.get('score'))
    print('state = {} , score = {} , cost = {} '.format(sol.get('state'), sol.get('score'), sol.get('cost')))

fig = plt.figure()
plt.plot(mutation_rate, costs, label='cost')
plt.plot(mutation_rate, scores, label='fitness')
fig.suptitle('Impact of increasing mutation rate', fontsize=12)
plt.xlabel('mutation rate', fontsize=8)
plt.ylabel('value', fontsize=8)
fig.savefig('2_genetic_b')
plt.legend()
plt.show()
