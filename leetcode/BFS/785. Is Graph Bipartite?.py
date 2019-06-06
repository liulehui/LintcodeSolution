class Solution:
    
    # BFS
    def isBipartite(self, graph: List[List[int]]) -> bool:
        UNSEEN = 0
        RED = 1
        BLUE = -1
        from collections import deque
        q = deque([])
        coloring = [0] * len(graph)

        for i in range(len(graph)):
            #  if it's already been seen, then skip
            if coloring[i] != UNSEEN:
                continue
            q.append(i)
            coloring[i] = RED

            while q:
                cur_vertice = q.popleft()
                for nei in graph[cur_vertice]: # neighbors
                    if coloring[nei] == 0:
                        coloring[nei] = -coloring[cur_vertice]
                        q.append(nei)
                    elif coloring[nei] != -coloring[cur_vertice]:
                        return False
        return True

#     # DFS
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         coloring = [0] * len(graph)
#         def dfs(cur):
#             for nei in graph[cur]:
#                 if coloring[nei] == UNSEEN:
#                     # If it hasn't been seen, then mark it as the opposite
#                     # of the current color, meaning, it must be in the opposite set
#                     coloring[nei] = -coloring[cur]
#                     if not dfs(nei):
#                         return False
#                 elif coloring[nei] != -coloring[cur]:
#                     return False
#             return True

#         for i in range(len(graph)):
#             if coloring[i] == UNSEEN:
#                 coloring[i] = RED
    #     if not dfs(i):
    #         return False
    # return True