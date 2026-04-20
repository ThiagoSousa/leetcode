class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[-1]*n for _ in range(n)]

        directions = ["right", "down", "left", "up"]
        d  = 0

        i = 0
        j = 0
        number = 1
        max_n = n**2
        while number<=max_n:
            matrix[i][j] = number
            number += 1
            if directions[d] == "right":
                j += 1
                if j>=n or matrix[i][j] != -1:
                    d = (d+1)%4
                    j -= 1
                    i += 1
                continue
            if directions[d] == "down":
                i += 1
                if i>=n or matrix[i][j] != -1:
                    d = (d+1)%4
                    i -= 1
                    j -= 1
                continue
            if directions[d] == "left":
                j -= 1
                if j<0 or matrix[i][j] != -1:
                    d = (d+1)%4
                    j += 1
                    i -= 1
                continue
            if directions[d] == "up":
                i -= 1
                if i<0 or matrix[i][j] != -1:
                    d = (d+1)%4
                    i += 1
                    j += 1
                continue
        print(matrix)
        return matrix