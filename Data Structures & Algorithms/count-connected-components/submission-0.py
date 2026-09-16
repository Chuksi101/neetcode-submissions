class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyMap = {i: [] for i in range(n)}
        for node, nei in edges:
            adjacencyMap[node].append(nei)
            adjacencyMap[nei].append(node)

        visited = set()
        
        def bfs(node):
            nonlocal visited
            q = deque([node])
            visited.add(node)
            while q:
                cur = q.popleft()
                for nei in adjacencyMap[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        return res