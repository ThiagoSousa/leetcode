class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(3):
            for j in range(index, len(nums)):
                if nums[j] == i:
                    aux = nums[index]
                    nums[index] = nums[j]
                    nums[j] = aux
                    index += 1