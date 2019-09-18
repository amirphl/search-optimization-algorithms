def list_contains_state(state, queue):
    for node in queue:
        if node.state == state:
            return True
    return False
