class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        matrix = [[0]*m for i in range(n)]

        assign = 1
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                assign = 0
            matrix[i][0] = assign
        print(matrix)
        
        assign = 1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                assign = 0
            matrix[0][i] = assign
        print(matrix)

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return matrix[-1][-1]
        

                
            