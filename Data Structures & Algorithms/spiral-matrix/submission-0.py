class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        # Potentially, could need <= instead of <
        while top < bottom and left < right:
            # Go right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # Go down
            for j in range(top, bottom):
                res.append(matrix[j][right-1])
            right -= 1

            # Check if bounds are still valid
            if not (top < bottom and left < right):
                break

            # Go left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # Go up
            for j in range(bottom-1, top-1, -1):
                res.append(matrix[j][left])
            left += 1
            print(left,right)

        return res
