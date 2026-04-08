class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]

        left = 0
        right = len(nums)-1

        while left <= right:
            middle = left + int((right-left)/2)

            if nums[middle] == target:
                start = middle
                end = middle
                while start>=0 and nums[start] == target:
                    start -= 1
                while end<len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]

            if nums[middle]<target:
                left = middle + 1
            else:
                right = middle - 1

        return [-1,-1]