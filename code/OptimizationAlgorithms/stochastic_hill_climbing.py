def stochastic_hill_climbing(problem):
    expanded = 0
    visited = 1
    current = problem.initialState
    solution = [current]
    while True:
        expanded += 1
        neighbor, num = problem.random_successor_v1(current)
        visited += num
        if neighbor.get('value') >= current.get('value'):
            return {'expanded': expanded, 'visited': visited, 'solution': solution,
                    'local minimum': current.get('value')}
        current = neighbor
        solution.append(neighbor)
