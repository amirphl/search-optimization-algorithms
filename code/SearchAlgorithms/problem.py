from SearchAlgorithms.data_structures import Node, ANode


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


def child_node(problem, parent, action):
    node = Node()
    node.state = problem.result(parent.state, action)
    node.parent = parent
    node.action = action
    node.path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    return node


def child_gnode(problem, parent, action):
    node = ANode()
    node.state = problem.result(parent.state, action)
    node.parent = parent
    node.action = action
    node.path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    node.heuristic_cost = problem.heuristic_cost(node.state)
    return node


def child_anode(problem, parent, action):
    node = ANode()
    node.state = problem.result(parent.state, action)
    node.parent = parent
    node.action = action
    node.path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    node.heuristic_cost = node.path_cost + problem.heuristic_cost(node.state)
    return node
