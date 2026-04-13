class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d: 
                for j in d[nums[i]]:
                    if abs(i-j)<=k:
                        return True
            else:
                d[nums[i]] = []
            d[nums[i]].append(i)
        return False
