class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        search = [(0,1), (-1,0), (1,0), (0,-1)]
        maxy = len(board)
        maxx = len(board[0])

        def backtrack(x,y,ind):
            if ind == len(word):
                return True

            if x < 0 or x >= maxx or y < 0 or y >= maxy or board[y][x] != word[ind]:
                return False

            if (x,y) not in visited:
                visited.add((x,y))
                for pair in search:    
                    if backtrack(x+pair[0], y+pair[1], ind+1):
                        return True
                visited.remove((x,y))

        for i in range(maxy):
            for j in range(maxx):
                if backtrack(j,i,0):
                    return True

        return False