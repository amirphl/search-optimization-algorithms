from OptimizationAlgorithms import genetic as g
from problem3 import problem as p
import matplotlib.pyplot as plt

pr = p.Problem()

population_size = 1000
number_of_generations = 20
mutation_rate = 0.02
tornument_size = [2, 5, 10]
plot = False

costs = []
scores = []
for t_siz in tornument_size:
    sol = g.genetic(pr, population_size, number_of_generations, mutation_rate, t_siz, plot)
    costs.append(sol.get('cost'))
    scores.append(sol.get('score'))
    print('state = {} , score = {} , cost = {} '.format(sol.get('state'), sol.get('score'), sol.get('cost')))

fig = plt.figure()
plt.plot(tornument_size, costs, label='cost')
plt.plot(tornument_size, scores, label='fitness')
fig.suptitle('Impact of increasing tornument size', fontsize=12)
plt.xlabel('tornument size', fontsize=8)
plt.ylabel('value', fontsize=8)
fig.savefig('3_genetic_c_3')
plt.legend()
plt.show()
