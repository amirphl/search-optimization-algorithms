class Problem():
    initialState = 1
    goalState = 8
    constant_step_cost = 1
    acts = {1: [2, 16, 18], 2: [3, 1], 3: [4, 2], 4: [5, 3], 5: [6, 4], 6: [7, 20, 5], 7: [8, 20, 6],
            8: [10, 19, 9, 7], 9: [8], 10: [11, 13, 8],
            11: [12, 10], 12: [11], 13: [14, 10], 14: [15, 13], 15: [14], 16: [17, 1], 17: [18, 16],
            18: [19, 20, 17, 1], 19: [8, 18], 20: [6, 7, 18], }
    h_cost = {1: 366, 2: 329, 3: 244, 4: 241, 5: 242, 6: 160, 7: 98, 8: 0, 9: 77, 10: 80, 11: 151, 12: 161, 13: 199,
              14: 226, 15: 234, 16: 374, 17: 380, 18: 253, 19: 178, 20: 193}

    def goal_test(self, state):
        if state == self.goalState:
            return True
        return False

    def actions(self, state):
        return self.acts.get(state)

    def result(self, state, action):
        return action

    def step_cost(self, state=None, action=None):
        return self.constant_step_cost

    def heuristic_cost(self, state):
        return self.h_cost.get(state)

    def heuristic_function(self):
        return self.h_cost
