class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        - m = len(matrix[0]), n = len(matrix)
        - initialize row and col
        - first, we check for the row
            - u = 0 and d = n
            - mid = u+d//2
            - if target >= matrix[mid][0] and <= matrix[mid][-1], we have the row
            - else, if less, r = mid or l = mid + 1
        - once we exit loop, if row is None: early exit
        - once we have row, repeat above for col
        - return col is not None
        '''
        m = len(matrix[0]) 
        n = len(matrix)
        row, col = None, None
        l, r =0, n 

        while l < r and row is None:
            mid = (l+r)//2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
            elif target < matrix[mid][0]:
                r = mid
            else:
                l = mid + 1

        if row is None:
            return False

        l, r =0, m-1
        while l <= r and col is None:
            mid = (l+r)//2

            if target == matrix[row][mid]:
                col = mid
            elif l == r:
                break
            elif target < matrix[row][mid]:
                r = mid
            else:
                l = mid + 1
        return col is not None
