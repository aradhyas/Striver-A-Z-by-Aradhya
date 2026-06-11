# here we are seeing that when edges = 1, odd possibility is 1, edges = 2, odd =2, edges = 3, odd = 4 and so on. so basically 2^edges/2 = gives the total odd answers

from collections import deque

def maxDepth(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    queue = deque()
    
    # start from node 1, depth 0
    queue.append((1, 0))
    visited[1] = True
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
                pass
    
    return max_depth

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        max_edges = maxDepth(len(edges)+1, edges)
        MOD = 10**9 + 7
        return pow(2, max_edges - 1, MOD)