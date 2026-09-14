class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = deque()

        left,right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        while up < down and left < right:
            for i in range(left,right):
                temp.append(matrix[up][i])
            matrix[up][right-1] = temp.popleft()
            for j in range(up+1, down):
                temp.append(matrix[j][right-1])
                matrix[j][right-1] = temp.popleft()
            # process going left
            for i in range(right-2, left - 1, -1):
                temp.append(matrix[down-1][i])
                matrix[down-1][i] = temp.popleft()
            # process going up
            for j in range(down-2, up - 1, -1):
                temp.append(matrix[j][left])
                matrix[j][left] = temp.popleft()
            # process going right
            for i in range(left+1,right):
                matrix[up][i] = temp.popleft()
            up += 1
            left += 1
            down -= 1
            right -= 1
