def hill_climbing(problem):
    expanded = 0
    visited = 1
    current = problem.initialState
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
