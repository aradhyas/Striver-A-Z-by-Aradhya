from collections import deque
import math

class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = max(1, math.floor(math.log2(n)) + 1)
        
        # build graph
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # bfs to get depth and parent
        depth = [0] * (n + 1)
        up = [[-1] * (n + 1) for _ in range(LOG)]  # up[j][v] = 2^j-th ancestor
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[node] + 1
                    up[0][neighbor] = node  # direct parent
                    queue.append(neighbor)
        
        # build binary lifting table
        for j in range(1, LOG):
            for v in range(1, n + 1):
                if up[j-1][v] != -1:
                    up[j][v] = up[j-1][up[j-1][v]]
        
        # lca using binary lifting
        def lca(u, v):
            # make u the deeper node
            if depth[u] < depth[v]:
                u, v = v, u
            
            # bring u up to same depth as v
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:  # if j-th bit is set
                    u = up[j][u]
            
            if u == v:
                return u
            
            # move both up until they meet
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            
            return up[0][u]
        
        # answer queries
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
            l = lca(u, v)
            path_length = depth[u] + depth[v] - 2 * depth[l]
            answer.append(pow(2, path_length - 1, MOD))
        
        return answer