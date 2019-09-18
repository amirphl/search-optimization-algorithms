class Problem:
    initialState = 0

    def goal_test(self, state):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def step_cost(self, state, action):
        pass

    def heuristic_cost(self, state):
        pass

    def heuristic_function(self):
        pass

    def objective_function(self):
        pass

    def highest_value_successor(self, state):
        return 1, 2

    def random_successor(self, state):
        return 1

    def first_choice_successor(self, state):
        return 1

    def generate_random_state(self):
        pass
