import sys


class Node:
    parent = None
    state = 0
    path_cost = 0
    action = None

    def __gt__(self, other):
        return self.path_cost > other.path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __eq__(self, other):
        return self.path_cost == other.path_cost


class ANode(Node):
    heuristic_cost = sys.maxsize

    def __gt__(self, other):
        return self.heuristic_cost > other.heuristic_cost

    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost

    def __eq__(self, other):
        return self.heuristic_cost == other.heuristic_cost


class Failure:
    def __str__(self):
        return 'Failure class'


class CutOff:
    def __str__(self):
        return 'CutOff class'


class Solution:
    visited = 0
    expanded = 0
    max_memory = 0
    best_path = []
    path_cost = 0

    # todo check order of traverse
    def find_path(self, last_node):
        self.best_path.append(last_node)
        parent = last_node.parent
        while parent is not None:
            self.best_path.append(parent)
            parent = parent.parent

    def add_node_to_best_path(self, node):
        self.best_path.append(node)
