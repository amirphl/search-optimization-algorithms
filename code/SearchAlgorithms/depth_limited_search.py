from SearchAlgorithms.data_structures import Node, Solution, CutOff, Failure
from SearchAlgorithms.problem import child_node


def depth_limited_search(problem, limit):
    node = Node()
    node.state = problem.initialState
    return recursive_depth_limited_search(node, problem, limit)


# todo visited
# todo expanded
# todo memory
def recursive_depth_limited_search(node, problem, limit):
    if problem.goal_test(node.state):
        sol = Solution()
        sol.visited = 1
        sol.path_cost = node.path_cost
        sol.best_path = [node]
        return sol, None, None
    elif limit == 0:
        return CutOff(), 1, 0
    else:
        visited = 1
        expanded = 1
        cutoff_occurred = False
        for action in problem.actions(node.state):
            if node.parent is not None and action == node.parent.state:
                continue
            child = child_node(problem, node, action)
            result, v, e = recursive_depth_limited_search(child, problem, limit - 1)
            if isinstance(result, CutOff):
                cutoff_occurred = True
                visited += v
                if e is not None:
                    expanded += e
            elif not isinstance(result, Failure):
                result.add_node_to_best_path(node)
                result.visited += visited
                result.expanded += expanded
                return result, None, None
        if cutoff_occurred:
            return CutOff(), visited, expanded
        else:
            return Failure(), visited, expanded
