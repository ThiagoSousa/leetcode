class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        n = len(a)
        m = len(b)

        if n<m:
            a = "0"*(m-n)+a
            n = m
        elif m<n:
            b = "0"*(n-m)+b
            m = n

        rest = 0
        result = []
        for i in range(n-1, -1, -1):
            digit_a = int(a[i])
            digit_b = int(b[i])
            s = (digit_a+digit_b+rest)%2
            rest = int((digit_a+digit_b+rest)/2)
            result.append(str(s))
        
        if rest:
            result.append("1")
        return "".join(result[::-1])

