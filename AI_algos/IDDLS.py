



# def iddfs(graph, start, goal, max_limit):
#     for limit in range(max_limit + 1):   # gradually increase depth
#         print(f"\nSearching with depth limit = {limit}")
#         if dls(graph, start, goal, limit):
#             print(f"✔ Found {goal} within depth {limit}")
#             return
#     print("Goal not found within given limit")

# def dls(graph, start, goal, limit):
#     stack = [(start, 0)]
#     visited = [start]
#
#     while stack:
#         node, depth = stack   .pop()   # DFS → use pop()
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





def iddfs(graph, start, goal, limiter):
    queue = [(start, 0)]
    visited = [start]

    while queue:
        node, depth = queue.pop()

        if node == goal:
            print("Goal is : ", node, ' at limiter : ', limiter)
            return

        if depth < limiter:
            for child in reversed(graph[node]):
                if child not in visited:
                    queue.append((child, depth + 1))
                    visited.append(child)
    print("Goal ", goal, " is beyond your limiter : ", limiter)


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

limiter = int(input("Enter the limiter number :   "))

for lim in range(0, limiter + 1):
    iddfs(graph, 'A', 'J', lim)

