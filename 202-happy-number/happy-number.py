class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True
            if n in d:
                return False
            d[n] = 0
            