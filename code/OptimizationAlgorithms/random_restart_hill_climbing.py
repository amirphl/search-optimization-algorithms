def random_restart_hill_climbing(problem, steps):
    solution = start(problem)
    visited = solution.get('visited')
    expanded = solution.get('expanded')
    for i in range(steps - 1):
        sol = start(problem)
        visited += sol.get('visited')
        expanded += sol.get('expanded')
        if solution.get('local minimum') >= sol.get('local minimum'):
            solution = sol

    return {'visited': visited, 'expanded': expanded, 'local minimum': solution.get('local minimum'),
            'solution': solution.get('solution')}


def start(problem):
    expanded = 0
    visited = 1
    current = problem.generate_random_state_v1()
    solution = [current]
    while True:
        neighbor, num = problem.lowest_value_successor(current)
        expanded += 1
        visited += num
        if neighbor.get('value') >= current.get('value'):
            return {'expanded': expanded, 'visited': visited, 'solution': solution,
                    'local minimum': current.get('value')}
        current = neighbor
        solution.append(neighbor)
