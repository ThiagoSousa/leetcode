class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        print(m,n)

        left = 0
        right = m*n-1

        while left<=right:
            middle = left + int((right-left)/2)

            i = int(middle/n)
            j = middle%n

            # print(m, n, left, right, middle, i, j)

            if matrix[i][j] == target:
                return True

            if matrix[i][j]>target:
                right = middle-1
            if matrix[i][j]<target:
                left = middle+1
        return False
