class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = max(nums)
        for i in range(max_n+1):
            if i not in nums:
                return i
        return max_n+1