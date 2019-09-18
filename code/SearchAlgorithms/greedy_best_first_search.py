import queue as q
from SearchAlgorithms.utils import list_contains_state
from SearchAlgorithms.data_structures import ANode, Failure, Solution

from SearchAlgorithms.problem import child_gnode


def greedy_best_first_search(problem):
    node = ANode()
    node.state = problem.initialState
    frontier = q.PriorityQueue()
    frontier.put(node)
    visited = 1
    explored = []
    while True:
        if frontier.empty():
            return Failure()
        node = frontier.get()
        if problem.goal_test(node.state):
            sol = Solution()
            sol.visited = visited
            sol.expanded = len(explored)
            sol.path_cost = node.path_cost
            sol.max_memory = frontier.qsize() + len(explored)
            sol.find_path(node)
            return sol
        explored.append(node)
        for action in problem.actions(node.state):
            child = child_gnode(problem, node, action)
            if not list_contains_state(child.state, frontier.queue) \
                    and not list_contains_state(child.state, explored):
                frontier.put(child)
                visited += 1
