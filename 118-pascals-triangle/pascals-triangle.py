class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1,1]]
        
        output = [[1], [1,1]]
        for i in range(numRows-2):
            last_row = output[-1]
            new_row = [1]
            for j in range(len(last_row)-1):
                new_row.append(last_row[j]+last_row[j+1])
            new_row.append(1)
            output.append(new_row)
        return output
        