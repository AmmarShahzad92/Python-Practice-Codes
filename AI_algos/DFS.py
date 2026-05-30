
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

