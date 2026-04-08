class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()

        for n in nums:
            if n>0:
                s.add(n)

        smallest_positive = 1
        while smallest_positive in s:
            smallest_positive += 1
        return smallest_positive