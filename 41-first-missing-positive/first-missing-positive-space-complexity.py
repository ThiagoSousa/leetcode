class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = {}

        for n in nums:
            if n>0:
                s[n] = 0

        smallest_positive = 1
        while smallest_positive in s:
            smallest_positive += 1
        return smallest_positive
