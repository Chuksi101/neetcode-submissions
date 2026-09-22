class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        - Use variables to define the bounds (down &right)
        - Initialize 2 sets (1 for pacific and 1 for atlantic)
        - Initialize a result list
        -> Overall idea is that we check the cells that are reachable from pacific (and add to set) and repeat for Atlantic and then we take the cells that are reachable from both and return those (append to result list)
            - we need to pass in current cell position {r,c}, set being used and prevHeight
            - boundary check
                - don't forget to return early if in visited set
            - add to visited set
            - run dfs on all directions
        - Loop for the columns (0 for Pacific and down-1 for atlantic)
        - Loop for the rows (0 for Pacific and right)
        - Get intersection of both sets (for loop through one and append to res if in the other)
        '''
        maxR = len(heights)
        maxC = len(heights[0])
        atl, pac = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r >= maxR or c >= maxC or (r,c) in visited or heights[r][c] < prevHeight:
                return

            visited.add((r,c))
            pH = heights[r][c]

            dfs(r-1, c, visited, pH)
            dfs(r+1, c, visited, pH)
            dfs(r, c-1, visited, pH)
            dfs(r, c+1, visited, pH)

        for i in range(maxR):
            dfs(i, 0, pac, 0)
            dfs(i, maxC-1, atl, 0)

        for i in range(maxC):
            dfs(0, i, pac, 0)
            dfs(maxR-1, i, atl, 0)

        for tup in atl:
            if tup in pac:
                res.append(tup)

        return res
