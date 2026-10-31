class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        i = 0
        start = nums[i]
        while i<len(nums):
            if nums[i]==target:
                return True
            if i<len(nums)-1 and nums[i]>nums[i+1]:
                pivot = nums[i]
                if target>=start and target<=pivot:
                    return False
            i += 1
        return False
