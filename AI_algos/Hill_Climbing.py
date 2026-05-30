
def Hill_Climbing(graph, start, cost, goal):    #Hill Climb with max cost
    node = start
    current_cost = cost
    while True:
        if node == goal:
            print(node, "  ", current_cost)
            return
        children = graph.get(node, {})
        if not children:
            break
        node, best_cost = max(children.items(),key=lambda x:x[1])
        if best_cost <= current_cost:
            break
        current_cost = best_cost
    print("No")


def hill_climbing(graph, start, cost, goal):    #Hill Climb with min cost
    node = start
    current_cost = cost
    while True:
        if node == goal:
            print(node, "  ", current_cost)
            return
        children = graph.get(node, {})
        if not children:
            break
        node, best_cost = min(children.items(), key=lambda x:x[1])
        if best_cost >= current_cost:
            break
        current_cost = best_cost
    print("No")


# main

graph = {
    'S': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 2, 'E': 10},
    'D': {'E': 1},
    'F': {'G': 16},
    'E': {'G': 13},
    'G': {}
}


Hill_Climbing(graph, 'S', 2, 'E')
hill_climbing(graph, 'S', 4, 'E')
