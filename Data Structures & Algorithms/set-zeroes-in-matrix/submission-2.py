class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        - Initialize a variable (first row) for knowing if we're setting the first row to 0s
        -> We're goin to use the first column and row as the store for the rows and columns we are going to set to 0
        - loop through each cell, if it contains a 0 then set that row in the 0th column to 0 and that column in the 0th row to 0
            -> if the 0 exists on the top row matrix [0] [i], then use the first row 0 variable
        - Loop again through each cell and change to 0 if that row or column should be 0
        - if firstRow0, change all in the 0th row to 0
        '''

        firstRow0 = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow0 = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for k in range(len(matrix)):
                matrix[k][0] = 0

        if firstRow0:
            for k in range(len(matrix[0])):
                matrix[0][k] = 0
