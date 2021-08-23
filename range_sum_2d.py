class NumMatrix:

    def __init__(self, matrix):
        self.M = matrix
        self.rsum 

    def update(self, row, col, val):
        self.M[row][col] = val 

    def sumRegion(self, row1, col1, row2, col2):
        sum = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sum += self.M[i][j]

        return sum

