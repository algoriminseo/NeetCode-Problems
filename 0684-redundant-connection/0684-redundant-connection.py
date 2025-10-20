# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n + 1)]
        
        def dfs(node, par):
            #How to detect cycle with edges?
            if visit[node]:
                return True
            visit[node] = True
            for neighbor in adj_list[node]:
                if neighbor == par:
                    continue
                if dfs(neighbor, node):
                    return True
            return False

        #Limitation : does not know how to connect adj_list with Cycle
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]
        return []
        

       





