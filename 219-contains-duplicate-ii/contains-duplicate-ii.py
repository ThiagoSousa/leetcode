class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = set()
        # left = 0
        # right = 0
        # while right<=k and right<len(nums):
        #     if nums[right] in d:
        #         return True
        #     d.add(nums[right])
        #     right+=1
        # while right<len(nums):
        #     print(right, d)
        #     d.remove(nums[left])
        #     left += 1
        #     if nums[right] in d:
        #         return True
        #     right += 1
        #     d.add(nums[right])            
            
        # return False

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



