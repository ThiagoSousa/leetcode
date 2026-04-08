class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n == 2:
            return 2

        dp_vector = [0]*(n+1)
        dp_vector[1] = 1
        dp_vector[2] = 2
        for i in range(3,n+1):
            dp_vector[i] = dp_vector[i-1]+dp_vector[i-2]
        return dp_vector[-1]