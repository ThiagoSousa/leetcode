class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        rest = num%9
        if rest == 0:
            return 9
        return rest
