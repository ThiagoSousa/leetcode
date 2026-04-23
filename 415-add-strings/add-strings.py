class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num2)>len(num1):
            aux = num1
            num1 = num2
            num2 = aux
        num2 = "0"*(len(num1)-len(num2))+num2

        n = len(num1)
        rest = 0
        result = []
        for i in range(n-1, -1, -1):
            s = int(num1[i])+int(num2[i])+rest            
            rest = int(s/10)
            s = s%10
            result.append(str(s))
        if rest>0:
            result.append(str(rest))
        return "".join(result[::-1])
