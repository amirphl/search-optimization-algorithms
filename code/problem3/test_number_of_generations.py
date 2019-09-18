from OptimizationAlgorithms import genetic as g
from problem3 import problem as p
import matplotlib.pyplot as plt

pr = p.Problem()

population_size = 100
number_of_generations = [50, 500, 5000]
mutation_rate = 0.02
tornument_size = 4
plot = False

costs = []
scores = []
for number in number_of_generations:
    sol = g.genetic(pr, population_size, number, mutation_rate, tornument_size, plot)
    costs.append(sol.get('cost'))
    scores.append(sol.get('score'))
    print('state = {} , score = {} , cost = {} '.format(sol.get('state'), sol.get('score'), sol.get('cost')))

fig = plt.figure()
plt.plot(number_of_generations, costs, label='cost')
plt.plot(number_of_generations, scores, label='fitness')
fig.suptitle('Impact of increasing number of generations', fontsize=12)
plt.xlabel('number of generations', fontsize=8)
plt.ylabel('value', fontsize=8)
fig.savefig('3_genetic_a')
plt.legend()
plt.show()
