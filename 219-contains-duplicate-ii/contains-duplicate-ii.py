class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if i>k:
                del d[nums[i-k-1]]
            if nums[i] in d:
                return True
            d[nums[i]] = 0
        return False        



