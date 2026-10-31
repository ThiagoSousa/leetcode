class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        if n%2==0:
            temp = self.myPow(x, int(n/2))
            return temp*temp
        else:
            temp = self.myPow(x, int((n-1)/2))
            return x*temp*temp
