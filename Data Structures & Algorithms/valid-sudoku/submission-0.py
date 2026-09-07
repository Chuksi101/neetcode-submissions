class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows {For loop through board, ensure max(Counter.Values) < 2}
            #Initialize a dict with keys 1 through 9 and store each value seen in a set from the row in the respective column
            # Check all columns {ensure that a value is not already in the set}
            # Since we know that index 0, 3, 6 are the beginning of the 3x3 box, we can store each result we see in a separate set for the 3x3 check and we would re initialize at 2,2 or any +3 multiple/permutation
                # for each i and j, once we are index 2,2 | 5,2 | 8,2 or like 2,5, 5,5 etc

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board[0])):
            for j in range(len(board)):
                curr = board[j][i]
                if curr in rows[j]:
                    print(curr, i, j)
                    print(rows)
                    return False
                elif curr in cols[i]:
                    print(curr, i, j)
                    print(cols)
                    return False
                box = (j // 3) * 3 + (i // 3)
                if curr in boxes[box]:
                    print(curr, i, j)
                    print(boxes)
                    return False
                
                if curr != '.':
                    cols[i].add(curr)
                    rows[j].add(curr)
                    boxes[box].add(curr)

        return True

