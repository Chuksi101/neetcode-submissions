class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            Check len(edges) == n - 1.
            Build an undirected adjacency map.
                start with
                    graph = {i: [] for i in range(n)}
            Initialize visited.
            Run dfs(0, parent).
            During DFS:
                unvisited neighbor → recurse
                visited neighbor that isn't the parent → cycle → False
            After DFS, check len(visited) == n.
        '''
        if len(edges) >= n:
            return False
        
        graph = {i: [] for i in range(n)}
        for nd, nei in edges:
            graph[nd].append(nei)
            graph[nei].append(nd)

        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for i in graph[node]:
                if i in visited and i != parent:
                    return False
                elif i not in visited:
                    dfs(i, node)

        dfs(0, None)

        return len(visited) == n