class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        all_sum = int((n*n+n)/2)
        nums_sum = sum(nums)
        diff = all_sum-nums_sum
        if 0 not in nums:
            return 0
        if diff == 0:
            return n+1
        return diff
