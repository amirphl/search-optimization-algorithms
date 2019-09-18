from SearchAlgorithms.depth_limited_search import depth_limited_search
from SearchAlgorithms.data_structures import Solution, Failure, CutOff


# todo statistics
def iterative_deepening_depth_first_search(problem, limit):
    cutoff_occurred = False
    v_total = 0
    e_total = 0
    v_total_f = 0
    e_total_f = 0
    for i in range(0, limit + 1):
        result, v, e = depth_limited_search(problem, i)
        if isinstance(result, CutOff):
            cutoff_occurred = True
            v_total += v
            e_total += e
        elif isinstance(result, Solution):
            return result, v, e
        elif isinstance(result, Failure):
            v_total_f += v
            e_total_f += e
    if cutoff_occurred:
        return CutOff(), v_total, e_total
    else:
        return Failure(), v_total_f, e_total_f
