class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n<=0:
        #     return False
        # while n%4==0:
        #     n = int(n/4)
        # return n==1
        if n<=0:
            return False
        return (n & (n-1)) == 0 and n%3==1
