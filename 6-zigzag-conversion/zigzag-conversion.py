class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        output = ""
        for i in range(numRows):
            j = i
            zig = True if i<numRows-1 else False
            while j<len(s):
                output += s[j]
                if zig:
                    j += (numRows-i-1)*2
                    if i>0:
                        zig = False
                else:
                    j += i*2
                    if i < numRows-1:
                        zig = True
        return output




            

            