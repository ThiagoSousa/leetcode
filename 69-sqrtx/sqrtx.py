class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        # for i in range(1,x+1):
        #     if i*i > x:
        #         return i-1
        left = 1
        right = x-1
        result = -1
        while left<=right:
            middle = left+int((right-left)/2)
            print(left, right, middle)
            middle_sq = middle*middle
            if middle_sq == x:
                return middle
            elif middle_sq > x:
                right = middle - 1
            else:
                result = middle
                left = middle + 1
        return result
            