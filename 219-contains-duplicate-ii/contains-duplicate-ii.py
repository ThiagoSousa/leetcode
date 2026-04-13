class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(k+1):
            if i>=len(nums):
                return False
            if nums[i] in d:
                return True
            d[nums[i]] = 0

        left = 0
        for i in range(k+1, len(nums)):
            del d[nums[left]]
            left += 1

            if nums[i] in d:
                return True
            d[nums[i]] = 0
        return False



