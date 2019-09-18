from random import randint, choice
import matplotlib.pyplot as plt
import sys


def genetic(problem, population_size, number_of_generations, mutation_rate, tornument_size, plot=True):
    population = problem.generate_population(population_size)
    worst_fitness = []
    average_fitness = []
    best_fitness = []
    for j in range(number_of_generations):
        parents = tornument_selection(population, tornument_size)
        childes = []
        w_fitness = sys.maxsize
        a_fitness = 0
        b_fitness = -1
        for i in range(population_size):
            x = random_selection(parents, None)
            y = random_selection(parents, x)
            child = crossover(x, y, problem.fitness_function)
            childes.append(child)
            a_fitness += child.get('value')
            if child.get('value') > b_fitness:
                b_fitness = child.get('value')
            if child.get('value') < w_fitness:
                w_fitness = child.get('value')
        mutate(childes, mutation_rate, problem.V, problem.upper_bound, problem.lower_bound,
               problem.fitness_function)
        population = childes
        a_fitness = 1.0 * a_fitness / len(childes)
        worst_fitness.append(w_fitness)
        average_fitness.append(a_fitness)
        best_fitness.append(b_fitness)

    if plot:
        fig = plt.figure()
        plt.plot(range(number_of_generations), worst_fitness, label='worst')
        plt.plot(range(number_of_generations), average_fitness, label='average')
        plt.plot(range(number_of_generations), best_fitness, label='best')
        fig.suptitle('Best,Average,Worst of Eligibility', fontsize=20)
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('value', fontsize=16)
        fig.savefig('2_genetic_a')
        plt.legend()
        plt.show()

    return best_in_population(population, problem.cost)


def tornument_selection(population, tornument_size):
    population = population[:]
    parents = []
    iterations = int(len(population) / tornument_size)
    for i in range(iterations):
        temp = []
        for j in range(tornument_size):
            n = randint(0, len(population) - 1)
            temp.append(population[n])
        u = temp[0]
        for k in temp:
            if k.get('value') > u.get('value'):
                u = k
        parents.append(u)
        population.remove(u)
    return parents


def random_selection(population, exception):
    r = randint(0, len(population) - 1)
    if exception is not None and population[r] == exception:
        return population[(r + 1) % len(population)]
    return population[r]


def crossover(x, y, fitness_function):
    n = len(x.get('state'))
    c = randint(0, n - 1)
    z = concat(x.get('state'), y.get('state'), c)
    return {'state': z, 'value': fitness_function(z)}


def concat(x_state, y_state, c):
    return x_state[0:c] + y_state[c:]


def mutate(population, mutation_rate, number_of_genomes, upper_bound, lower_bound, fitness_function):
    mutated_genomes = int(len(population) * number_of_genomes * mutation_rate)
    for i in range(mutated_genomes):
        r = randint(0, len(population) - 1)
        u = randint(0, number_of_genomes - 1)
        s = population[r].get('state')
        pc = s[u]
        list_1 = list(range(lower_bound, pc))
        list_2 = list(range(pc + 1, upper_bound + 1))
        if len(list_1) == 0 and len(list_2) == 0:
            c = pc
        elif len(list_1) != 0 and len(list_2) != 0:
            c = choice(list_1 + list_2)
        elif len(list_1) != 0:
            c = choice(list_1)
        else:
            c = choice(list_2)
        s[u] = c
        population[r] = {'state': s, 'value': fitness_function(s)}


def best_in_population(population, cost_function):
    if len(population) == 0:
        return None
    best = population[0]
    for individual in population:
        if cost_function(best) < cost_function(individual):
            best = individual
    return {'state': best.get('state'), 'cost': cost_function(best), 'score': best.get('value')}
