class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = len(nums)-1

        while left<right:
            middle = left+int((right-left)/2)

            if nums[middle]>nums[right]:
                left = middle+1
            else:
                right = middle

        k = right
        
        nums = nums[right:]+nums[:right]

        left = 0
        right = len(nums)-1
        while left<right:
            middle = left+int((right-left)/2)

            if nums[middle] == target:
                return (middle+k)%len(nums)

            if nums[middle]>target:
                right = middle
            else:
                left = middle+1

        if nums[right] == target:
            return (right+k)%len(nums)

        return -1
