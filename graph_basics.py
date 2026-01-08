from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()
    final_output = []

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        final_output.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
    return final_output


def dfs(graph, start):
    visited = set()
    final_output = []

    def check(node):
        visited.add(node)
        final_output.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                check(neighbour)

    check(start)
    return final_output



graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print(bfs(graph, 1))
print(dfs(graph, 1))