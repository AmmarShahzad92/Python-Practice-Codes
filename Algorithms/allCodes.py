
def bfs (graph, visited, queue, root):
    queue.append(root)
    visited.append(root)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.append(child)

# main

graph = {
    '5': ['3', '7', '9'],
    '3': ['6', '8'],
    '7': [],
    '8': ['8', '7', '2'],
    '9': ['1'],
    '6': [],
    '2': [],
    '1': []
}

bfs(graph, [], [], '5')


def dfs(graph, visited, stack, node):
    visited.append(node)
    stack.append(node)
    while stack:
        m = stack.pop()
        print(m , end = " ")
        for n in reversed(graph[m]):
            if n not in visited:
                visited.append(n)
                stack.append(n)



# main

graph = {
    '5': ['3', '7', '9'],
    '3': ['6', '8'],
    '7': [],
    '8': ['8', '7', '2'],
    '9': ['1'],
    '6': [],
    '2': [],
    '1': []
}


dfs(graph, [], [], '5')

import heapq


class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

def UcS(graph, start, Cost, goal):
    queue = [(Cost, start, [start])]
    while (queue):
        queue.sort()
        cost, node, path = queue.pop(0)
        if node == goal:
            print("Your goal  from ", start, " to ", goal, "has cost of ", cost, " with the path of ", path)
        for child, eCost in graph[node].items():
            queue.append((eCost + cost, child, path + [child]))



# graph = {
#     'A' : {'B' : 2, 'C' : 5, 'D' : 3},
#     'B' : {'G' : 3, 'E' : 1},
#     'C' : {'E' : 3, 'H' : 4},
#     'D' : {'I' : 2},
#     'G' : {'K' :  2, 'L' : 4},
#     'E' : {'F' : 2, 'J' : 7},
#     'H' : {'F' : 5, 'L' : 3},
#     'I' : {'J' : 5},
#     'K' : {'F' : 9},
#     'L' : {'J' : 3},
#     'F' : {'J' :1},
#     'J' : {}
# }

graph = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'F': {'G': 16},
    'E': {'G': 5},
    'G': {}
}

UcS(graph, 'S',  0, 'G')


import heapq


class Node:
    def __init__(self, node, cost, heur):
        self.node = node
        self.cost = cost
        self.heur = heur if heur is not None else 0

def a_star(graph, start, Cost, goal, heuristic):
    queue = [(heuristic[start] + Cost, Cost, start, [start])]
    while queue:
        queue.sort()
        heur, cost, node, path = queue.pop(0)
        if node == goal:
            print("Your cost from ", start, " to ", goal, " is", cost, "wih heuristic  ", heur, " with path ", path)
        for child, edgeCost in graph[node].items():
            hn = heuristic[child]
            gn = edgeCost + cost
            queue.append((hn + gn   , gn, child, path + [child]))



# main

graph = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'F': {'G': 16},
    'E': {'G': 5},
    'G': {}
}

heuristics = {
    'S': 10,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

a_star(graph, 'S', 0,  'G', heuristics)


import numpy as np

# Define the function
def f(x):
    return -(x-3)**2 +9  # Parabola with max at x = 3

# Hill Climbing Algorithm
def hill_climb(start_x, step_size = 0.1, max_iterations = 1000):
    x = start_x  # Fixed starting point
    for _ in range(max_iterations):
        next_x = x + step_size
        prev_x = x - step_size

        if f(next_x) > f(x):
            x = next_x
        elif f(prev_x) > f(x):
            x = prev_x
        else:
            break

    return x, f(x)

# Fixed starting point (not random anymore)
start_x = -5.0

# Run the hill climbing algorithm
x_max, f_max = hill_climb(start_x)

# Print results
print(f"Starting at x = {start_x:.2f}")
print(f"Maximum found at x = {x_max:.2f}, f(x) = {f_max:.2f}")
