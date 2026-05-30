



# def dls(graph, start, goal, limit):
#     stack = [(start, 0)]
#     visited = [start]
#
#     while stack:
#         node, depth = stack.pop()   # DFS → use pop()
#
#         if node == goal:
#             print("Goal is:", node, "at depth", depth)
#             return True
#
#         if depth < limit:
#             for child in reversed(graph[node]):  # reverse for DFS-like order
#                 if child not in visited:
#                     stack.append((child, depth + 1))
#                     visited.append(child)
#     return False






def dls(graph, start, goal, limiter):
    queue= [(start, 0)]
    visited = [start]

    while queue:
        node, depth = queue.pop()
        if node == goal:
            print("Goal is : ", node, " at limiter : ", limiter)
            return

        if depth < limiter:
            for child in reversed(graph[node]):
                if child not in visited:
                    queue.append((child, depth+ 1))
                    visited.append(child)
    print("Goal ", goal, " is beyond your limiter : ",limiter)

# main

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['G', 'E'],
    'C': ['E', 'H'],
    'D': ['I'],
    'G': ['K', 'L'],
    'E': ['F', 'J'],
    'H': ['F', 'L'],
    'I': ['J'],
    'K': ['F'],
    'L': ['J'],
    'F': ['J'],
    'J': []
}

dls(graph, 'A', 'J', 3)
