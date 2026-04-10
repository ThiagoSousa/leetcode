class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n>0:
            bits.append(n%2)
            n = int(n/2)
        if len(bits)<32:
            bits = bits+[0]*(32-len(bits))
        return sum([bit*2**i for i, bit in enumerate(bits[::-1])])