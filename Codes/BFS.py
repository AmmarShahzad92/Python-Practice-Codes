
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

