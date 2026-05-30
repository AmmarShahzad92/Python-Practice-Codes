import heapq


class Node: # Node Class Universal in all algorithms
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

def ucs(graph, start, cost, goal):  #UCS with History maintenance without heapq
    queue = [Node(start, cost)]
    visited = []
    while (queue):
        queue.sort(key=lambda node: node.cost)
        n = queue.pop(0)
        if (n.node not in visited):
            visited.append(n.node)
        if (n.node == goal):
            print("Your cost from ", start, " to ", goal, " is", n.cost)
            return

        for child, cCost in graph[n.node].items():
            if (child not in visited):
                queue.append(Node(child, n.cost + cCost))
    print("No Node is found of ", goal, ".")


def UCS(graph, start, Cost,  goal): #UCS with History maintenance with heapq
    queue = [(Cost, start)]
    visited = [start]

    while (queue):
        cost, node = heapq.heappop(queue)
        if node == goal:
            print("Your goal ", goal, "has cost of ", cost)
            return
        for child, eCost in graph[node].items():
            if (child not in visited):
                heapq.heappush(queue, (eCost + cost, child))
                visited.append(node)


def Ucs(graph, start, Cost,  goal): #UCS without History maintenance with heapq
    queue = [(Cost, start, [start])]

    while (queue):
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            print("Your goal  from ", start, " to ", goal, "has cost of ", cost, " with the path of ", path)
        for child, eCost in graph[node].items():
            heapq.heappush(queue, (eCost + cost, child, path + [child]))



def UcS(graph, start, Cost, goal):  #UCS without History maintenance without heapq
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
}   #graph for testing

UcS(graph, 'S',  0, 'G')
Ucs(graph, 'S', 0, 'G')
UCS(graph, 'S', 0, 'G')
ucs(graph, 'S', 0, 'G')