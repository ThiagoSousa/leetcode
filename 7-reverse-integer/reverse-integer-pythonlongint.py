class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        is_negative = True if "-" in str_x else False
        if is_negative:
            str_x = str_x[1:]
        str_x = str_x[::-1]
        if is_negative:
            reverse = int("-"+str_x)
        else:
            reverse = int(str_x)
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        return reverse
        

            
        
