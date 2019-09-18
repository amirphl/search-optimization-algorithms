import queue as q
from SearchAlgorithms.utils import list_contains_state
from SearchAlgorithms.data_structures import ANode, Failure, Solution

from SearchAlgorithms.problem import child_anode


def a_star(problem):
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
            child = child_anode(problem, node, action)
            if not list_contains_state(child.state, frontier.queue) \
                    and not list_contains_state(child.state, explored):
                frontier.put(child)
                visited += 1
            else:
                n = child_state_is_in_frontier_with_higher_cost(child, frontier.queue)
                if n is not None:
                    n.heuristic_cost = child.heuristic_cost
                    n.path_cost = child.path_cost
                    n.parent = child.parent
                    n.action = child.action


def child_state_is_in_frontier_with_higher_cost(child, frontier):
    for n in frontier:
        if n.state == child.state and n.heuristic_cost > child.heuristic_cost:
            return n
    return None
