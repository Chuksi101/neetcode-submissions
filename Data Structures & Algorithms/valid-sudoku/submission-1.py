class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board[0])):
            for j in range(len(board)):
                curr = board[j][i]
                if curr in rows[j]:
                    return False
                elif curr in cols[i]:
                    return False
                # The two pieces tell you which box row and which box column
                box = (j // 3) * 3 + (i // 3)
                if curr in boxes[box]:
                    return False
                
                if curr != '.':
                    cols[i].add(curr)
                    rows[j].add(curr)
                    boxes[box].add(curr)

        return True

