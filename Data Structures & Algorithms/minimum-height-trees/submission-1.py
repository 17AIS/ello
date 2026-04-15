class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neigh = defaultdict(list)
        minimal = float('inf')

        for i, j in edges:
            neigh[i].append(j)
            neigh[j].append(i)
        print(neigh)
        output = []

        for i in range(n):
            stack = [[i, 0]]
            mdepth = -1
            visited = [True] * n
            while stack:
                node, depth = stack.pop()
                visited[node] = False
                mdepth = max(depth, mdepth)
                for nei in neigh[node]:
                    if visited[nei]:
                        stack.append([nei, depth + 1])


            if minimal > mdepth:
                output = [i]
                minimal = mdepth
            elif minimal == mdepth:
                output.append(i) 

        return output