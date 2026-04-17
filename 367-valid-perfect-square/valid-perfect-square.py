import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = math.sqrt(num)
        if sqrt == int(sqrt):
            return True
        return False