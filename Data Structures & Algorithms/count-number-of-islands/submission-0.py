class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        search = [(0,1), (-1,0), (1,0), (0,-1)]

        maxh = len(grid)
        maxw = len(grid[0])

        for i in range(maxh):
            for j in range(maxw):
                if grid[i][j] == "1" and (i,j) not in visited:
                    stack = []
                    islands += 1
                    stack.append((i,j))
                    while stack:
                        y,x = stack.pop()
                        if x < 0 or x >= maxw or y < 0 or y >= maxh:
                            continue
                        if grid[y][x] == "1" and (y,x) not in visited:
                            visited.add((y,x))
                            for ind in search:
                                stack.append((y+ind[0], x+ind[1]))
        
        return islands
