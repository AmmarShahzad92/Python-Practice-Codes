import heapq


class Node: # Node Class Universal in all algorithms
    def __init__(self, node, cost, heur):
        self.node = node
        self.cost = cost
        self.heur = heur if heur is not None else 0 
        #here if heur is None, set self.heur to 0 to avoid errors thus temp check for if heur has no value

def A_Star(graph, start, cost, goal, heuristic):    #a* with history maintenance without heapq
    heur = heuristic[start]
    queue = [Node(start, cost, heur)]   #list of Node objects
    visited = []    #list of nodes i.e same as path in a* maintaining history

    while queue:
        # Sort the queue based on the f(n) = g(n) + h(n) value
        queue.sort(key=lambda node: node.heur + node.cost) # fn = hn(node.heur) + gn(node.cost)

        node = queue.pop(0)
        visited.append(node.node)
        if node.node == goal:
            print("Your cost from ", start, " to ", goal, " is", node.cost)
            return
        for child, edgeCost in graph[node.node].items():
            hn = heuristic[child]
            gn = edgeCost + node.cost
            if child not in visited:    # check if child node is already visited
                queue.append(Node(child, gn, hn + gn))

def A_STAR (graph, start, Cost, goal, heuristic):   #a* with history maintenance with heapq
    queue = [(heuristic[start], Cost, start)]
    visited = [start]

    while queue:
        heur, cost, node = heapq.heappop(queue)

        if node == goal:
            print("Your cost from ", start, " to ", goal, " is", cost)
            return

        for child, edgeCost in graph[node].items():
            hn = heuristic[child]
            gn = edgeCost + cost
            if child not in visited:
                heapq.heappush(hn + gn, gn, child)


def A_star (graph, start, Cost, goal, heuristic):   #a* without history maintenance with heapq
    queue = [(heuristic[start], Cost, start, [start])]

    while queue:
        heur, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Your cost from ", start, " to ", goal, " is", cost, "wih heuristic  ", heur, " with path ", path)

        for child, edgeCost in graph[node].items():
            hn = heuristic[child]
            gn = edgeCost + cost
            heapq.heappush(queue, (hn + gn, gn, child, path + [child]))


def a_star(graph, start, Cost, goal, heuristic):    #a* without history maintenance without heapq
    queue = [(heuristic[start] + Cost, Cost, start, [start])]
    while queue:
        queue.sort()
        heur, cost, node, path = queue.pop(0)
        if node == goal:
            print("Your cost from ", start, " to ", goal, " is", cost, "wih heuristic  ", heur, " with path ", path)
        for child, edgeCost in graph[node].items():
            hn = heuristic[child]   #heur cost of child node
            gn = edgeCost + cost    #cost till current node
            queue.append((hn + gn, gn, child, path + [child]))
            #queue.append(fn, gn, child, path)



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













import heapq

def a_star_optimal(graph, start, goal, heuristic):
    """Optimized A* with visited set to handle misleading nodes"""
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    best_cost = {}  # Track best cost to each node
    
    while queue:
        f_cost, g_cost, node, path = heapq.heappop(queue)
        
        # Skip if we've found a better path to this node
        if node in visited:
            continue
            
        visited.add(node)
        best_cost[node] = g_cost
        
        if node == goal:
            print(f"Optimal path: {' -> '.join(path)}")
            print(f"Total cost: {g_cost}")
            return path, g_cost
        
        for child, edge_cost in graph[node].items():
            if child not in visited:
                new_g_cost = g_cost + edge_cost
                new_f_cost = new_g_cost + heuristic[child]
                
                # Only add if we haven't seen this node or found better path
                if child not in best_cost or new_g_cost < best_cost[child]:
                    heapq.heappush(queue, (new_f_cost, new_g_cost, child, path + [child]))
    
    return None, float('inf')

def a_star_with_reopening(graph, start, goal, heuristic):
    """A* with node reopening for handling misleading paths"""
    queue = [(heuristic[start], 0, start, [start])]
    best_costs = {start: 0}  # Best known cost to reach each node
    
    while queue:
        f_cost, g_cost, node, path = heapq.heappop(queue)
        
        # Skip if we've found a better path to this node already
        if node in best_costs and g_cost > best_costs[node]:
            continue
            
        if node == goal:
            print(f"Path with reopening: {' -> '.join(path)}")
            print(f"Total cost: {g_cost}")
            return path, g_cost
        
        for child, edge_cost in graph[node].items():
            new_g_cost = g_cost + edge_cost
            
            # Add/update if this is a better path to child
            if child not in best_costs or new_g_cost < best_costs[child]:
                best_costs[child] = new_g_cost
                new_f_cost = new_g_cost + heuristic[child]
                heapq.heappush(queue, (new_f_cost, new_g_cost, child, path + [child]))
    
    return None, float('inf')

def a_star_depth_limited(graph, start, goal, heuristic, max_depth=15):
    """A* with depth limiting to prevent infinite loops"""
    queue = [(heuristic[start], 0, start, [start], 0)]  # Added depth counter
    visited = set()
    
    while queue:
        f_cost, g_cost, node, path, depth = heapq.heappop(queue)
        
        if depth > max_depth:
            continue
            
        state = (node, depth)  # Include depth in state
        if state in visited:
            continue
        visited.add(state)
        
        if node == goal:
            print(f"Depth-limited path: {' -> '.join(path)}")
            print(f"Total cost: {g_cost}, Depth: {depth}")
            return path, g_cost
        
        for child, edge_cost in graph[node].items():
            new_g_cost = g_cost + edge_cost
            new_f_cost = new_g_cost + heuristic[child]
            new_depth = depth + 1
            
            if new_depth <= max_depth:
                heapq.heappush(queue, (new_f_cost, new_g_cost, child, path + [child], new_depth))
    
    return None, float('inf')

def a_star_cycle_detection(graph, start, goal, heuristic):
    """A* with explicit cycle detection"""
    queue = [(heuristic[start], 0, start, [start])]
    
    while queue:
        f_cost, g_cost, node, path = heapq.heappop(queue)
        
        if node == goal:
            print(f"Cycle-safe path: {' -> '.join(path)}")
            print(f"Total cost: {g_cost}")
            return path, g_cost
        
        for child, edge_cost in graph[node].items():
            # Explicit cycle detection - don't revisit nodes in current path
            if child not in path:
                new_g_cost = g_cost + edge_cost
                new_f_cost = new_g_cost + heuristic[child]
                heapq.heappush(queue, (new_f_cost, new_g_cost, child, path + [child]))
    
    return None, float('inf')

# Test with the optimized graph
graph = {
    'S': {'B': 4, 'C': 3, 'D': 15},
    'B': {'F': 5, 'E': 12, 'C': 2},
    'C': {'D': 7, 'E': 10, 'B': 8},
    'D': {'E': 2, 'F': 6},
    'F': {'G': 16, 'E': 3},
    'E': {'G': 5, 'D': 4},
    'G': {}
}

heuristics = {
    'S': 12, 'B': 8, 'C': 9, 'D': 6, 'E': 4, 'F': 7, 'G': 0
}

print("=== Testing Optimized A* Variants ===")
print("\n1. Optimal A* (with visited set):")
a_star_optimal(graph, 'S', 'G', heuristics)

print("\n2. A* with Node Reopening:")
a_star_with_reopening(graph, 'S', 'G', heuristics)

print("\n3. A* with Depth Limiting:")
a_star_depth_limited(graph, 'S', 'G', heuristics)

print("\n4. A* with Cycle Detection:")
a_star_cycle_detection(graph, 'S', 'G', heuristics)