from random import randint, choice
import numpy as np


class Problem:
    """
    1 equals red
    2 equals green
    3 equals blue
    """
    initialState = {'state': [1, 2, 3, 3, 3, 1, 2, 2, 3, 3, 1], 'value': 4}
    graph = {1: [2, 3, 9, 11], 2: [4, 5, 1], 3: [6, 5, 1], 4: [7, 2, 11, 6], 5: [2, 3, 8, 10, 7], 6: [3, 8, 4, 9],
             7: [4, 5, 9], 8: [5, 6, 11], 9: [7, 10, 1, 6], 10: [9, 5, 11], 11: [10, 8, 4, 1], }
    colors = 3
    lower_bound = 1
    upper_bound = 3
    V = 11
    E = 20

    def cost(self, current):
        return self.objective_function(current.get('state'))

    @staticmethod
    def objective_function(state):
        mismatches = 0
        s = [-1] + state[:]
        if s[1] == s[2]:
            mismatches += 1
        if s[1] == s[3]:
            mismatches += 1
        if s[1] == s[9]:
            mismatches += 1
        if s[1] == s[11]:
            mismatches += 1
        if s[2] == s[4]:
            mismatches += 1
        if s[2] == s[5]:
            mismatches += 1
        if s[3] == s[5]:
            mismatches += 1
        if s[3] == s[6]:
            mismatches += 1
        if s[4] == s[6]:
            mismatches += 1
        if s[4] == s[7]:
            mismatches += 1
        if s[4] == s[11]:
            mismatches += 1
        if s[5] == s[7]:
            mismatches += 1
        if s[5] == s[8]:
            mismatches += 1
        if s[5] == s[10]:
            mismatches += 1
        if s[6] == s[8]:
            mismatches += 1
        if s[6] == s[9]:
            mismatches += 1
        if s[7] == s[9]:
            mismatches += 1
        if s[8] == s[11]:
            mismatches += 1
        if s[9] == s[10]:
            mismatches += 1
        if s[10] == s[11]:
            mismatches += 1
        return mismatches

    def lowest_value_successor(self, current):
        num = (self.colors - 1) * len(current.get('state'))
        result = {'state': current.get('state')[:], 'value': current.get('value')}
        for i in range(len(current.get('state'))):
            for co in range(self.colors):
                pc = current.get('state')[i]
                if co + 1 == pc:
                    continue
                current.get('state')[i] = co + 1
                cost = self.cost(current)
                if cost < result.get('value'):
                    result = {'state': current.get('state')[:], 'value': cost}
                current.get('state')[i] = pc
        return result, num

    def random_successor_v1(self, current):
        num = (self.colors - 1) * len(current.get('state'))
        standard = {'state': current.get('state')[:], 'value': current.get('value')}
        candidates = []
        inverse_of_costs = 0
        for i in range(len(current.get('state'))):
            for co in range(self.colors):
                pc = current.get('state')[i]
                if co + 1 == pc:
                    continue
                current.get('state')[i] = co + 1
                cost = self.cost(current)
                if cost < standard.get('value'):
                    candidates.append({'state': current.get('state')[:], 'value': cost})
                    inverse_of_costs += 1.0 / cost
                current.get('state')[i] = pc

        if len(candidates) == 0:
            return standard, num

        alpha = 1.0 / inverse_of_costs
        weights = []
        for x in candidates:
            weights.append(alpha / x.get('value'))

        sample = np.random.choice(len(candidates), 1000, p=weights)
        r = randint(0, 1000)
        best = sample[r]

        return candidates[best], num

    def random_successor_v2(self, current):
        num = 1
        pos = randint(0, self.V - 1)
        c = current.get('state')[pos]
        r = choice(list(range(1, c - 1)) + list(range(c + 1, self.colors + 1)))
        s = current.get('state')[:]
        s[pos] = r
        cost = self.objective_function(s)
        return {'state': s, 'value': cost}, num

    def first_choice_successor(self, current):
        num = 0
        init_cost = current.get('value')
        for i in range(len(current.get('state'))):
            for co in range(self.colors):
                pc = current.get('state')[i]
                if co + 1 == pc:
                    continue
                num += 1
                current.get('state')[i] = co + 1
                cost = self.cost(current)
                if cost < init_cost:
                    temp = {'state': current.get('state')[:], 'value': cost}
                    current.get('state')[i] = pc
                    return temp, num
                current.get('state')[i] = pc
        return current, num

    def generate_random_state_v1(self):
        state = []
        for i in range(self.V):
            c = randint(1, self.colors)
            state.append(c)
        cost = self.objective_function(state)
        return {'state': state, 'value': cost}

    @staticmethod
    def delta_function(i, j, state):
        return 1 if state[i] != state[j] else 0

    def fitness_function(self, state):
        t = 0
        for i in self.graph.keys():
            for j in self.graph.get(i):
                t += self.delta_function(i - 1, j - 1, state)
        return 1.0 * t / self.E

    def generate_random_state_v2(self):
        state = []
        for i in range(self.V):
            c = randint(1, self.colors)
            state.append(c)
        val = self.fitness_function(state)
        return {'state': state, 'value': val}

    def generate_population(self, pop_size):
        population = []
        for i in range(pop_size):
            population.append(self.generate_random_state_v2())
        return population
