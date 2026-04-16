class Solution:
    def addDigits(self, num: int) -> int:
        # while num>=10:
        #     num = sum([int(d) for d in str(num)])
        # return num
        if num == 0:
            return 0
        rest = num%9
        if rest == 0:
            return 9
        return rest