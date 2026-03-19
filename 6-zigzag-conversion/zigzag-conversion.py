class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        matrix = [[""]*len(s) for i in range(numRows)]
        
        zig = True
        i = 0
        j = 0
        for k in range(len(s)):
            matrix[i][j] = s[k]

            if zig:
                if i==numRows-1:
                    zig = False
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    zig = True
                    i += 1
                else:
                    i -=1
                    j += 1
        
        output = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != "":
                    output += matrix[i][j]

        return output



            

            