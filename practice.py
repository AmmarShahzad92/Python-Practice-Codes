# print ("Assalamu Alaikum dunya walo....")
graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : ['4'],
    '4' : ['8'],
    '8' : []
}

visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("BFS:", end=" ")
bfs(visited, graph, '5')
print("\nDFS:", end=" ")
visited = []  # Reset visited list before DFS
dfs(visited, graph, '5')
# print("\n")