class Solution:

    def rle(self, n:str) -> str:
        i = 0
        encoded = ""
        while i<len(n):
            j = i+1
            count = 1
            while j<len(n) and n[j] == n[i]:
                count += 1
                j += 1
            encoded += str(count)+n[i]
            i = j
        return encoded

    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        sequence = "1"
        for i in range(n-1):
            sequence = self.rle(sequence)
        return sequence
