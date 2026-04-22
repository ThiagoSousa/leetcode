class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        lines = set()
        columns = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    lines.add(i)
                    columns.add(j)

        for i in lines:
            for j in range(n):
                matrix[i][j] = 0
        
        for i in range(m):
            for j in columns:
                matrix[i][j] = 0
        