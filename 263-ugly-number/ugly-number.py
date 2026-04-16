import math
class Solution:

    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:
            flag = False
            if n%2==0:
                n = int(n/2)
                flag = True
            if n%3 == 0:
                n = int(n/3)
                flag = True
            if n%5 == 0:
                n = int(n/5)
                flag = True
            if not flag:
                return False
        return True
        