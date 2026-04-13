class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = set()
        left = 0
        right = k
        for i in range(left, right+1):
            if i>=len(nums):
                return False
            if nums[i] in d:
                return True
            d.add(nums[i])
        while right<len(nums):
            d.remove(nums[left])
            right += 1
            if right>=len(nums):
                return False
            left += 1
            if nums[right] in d:
                return True
            d.add(nums[right])
        return False

