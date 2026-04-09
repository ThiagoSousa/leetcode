class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        row = [1,2,1]
        for i in range(rowIndex-2):
            new_row = [1]
            for j in range(len(row)-1):
                new_row.append(row[j]+row[j+1])
            new_row.append(1)
            row = new_row
        return row