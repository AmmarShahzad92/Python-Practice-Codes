class Node:
    def __init__(self, node, cost, hval):
        self.node = node
        self.cost = cost
        self.hval = hval
def a_star(graph, start, Cost, goal, heur):
    queue = [(heur[start] + Cost, Cost, start, [start])]
    while queue:
        queue.sort()
        hval, cost, node, path = queue.pop(0)
        if node == goal:
            print("Total Cost =  ", cost, " from ", start, " to ", goal, " with heuristic ", hval, " with path ", path)
        for child, edgeCost in graph[node].items():
            hn = heur[child]
            gn = edgeCost + cost
            queue.append((hn + gn   , gn, child, path + [child]))



# main

graphs = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'F': {'G': 16},
    'E': {'G': 5},
    'G': {}
}

heurs = {
    'S': 10,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

a_star(graphs, 'S', 0,  'G', heurs)