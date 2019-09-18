from SearchAlgorithms.utils import list_contains_state
from SearchAlgorithms.data_structures import Node, Failure, Solution

from SearchAlgorithms.problem import child_node
import queue as q


def breadth_first_search(problem):
    node = Node()
    node.state = problem.initialState
    if problem.goal_test(node.state):
        sol = Solution
        sol.visited = 0
        sol.best_path = [node]
        return sol
    frontier = q.Queue()
    frontier.put(node)
    visited = 1
    explored = []
    while True:
        if frontier.qsize() == 0:
            return Failure()
        node = frontier.get()
        explored.append(node)
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)
            if not list_contains_state(child.state, frontier.queue) and not list_contains_state(child.state, explored):
                if problem.goal_test(child.state):
                    sol = Solution()
                    sol.visited = visited
                    sol.expanded = len(explored)
                    sol.path_cost = child.path_cost
                    sol.max_memory = frontier.qsize() + len(explored)
                    sol.find_path(child)
                    return sol
                frontier.put(child)
                visited += 1
