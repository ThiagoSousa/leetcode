class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        right = 1
        write = 0

        while right<len(nums):
            if nums[left] != nums[right]:
                nums[write] = nums[left]
                left += 1
                right += 1
                write += 1
            else:
                nums[write] = nums[left]
                write += 1
                while right<len(nums) and nums[left] == nums[right]:
                    right += 1
                left = right-1
        nums[write] = nums[left]
        return write+1

        
