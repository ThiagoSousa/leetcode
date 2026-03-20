class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip().rstrip()
        
        if len(s)==0:
            return 0
        
        is_negative = False
        i = 0
        if s[0] == "-":
            is_negative = True
            i = 1
        if s[0] == "+":
            is_negative = False
            i = 1
        
        digits = []
        while i<len(s):
            if ord(s[i])>=48 and ord(s[i])<=57:
                digits.append(s[i])
                i += 1
            else:
                break
                
        if len(digits)==0:
            return 0
                
        number = int("".join(digits))
        if is_negative:
            number = number * -1
            
        if number<-2**31:
            number = -2**31
        
        if number>2**31-1:
            number = 2**31-1
            
        return number
        