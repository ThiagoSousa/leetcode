class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solutions = []

        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i>0 and nums[i] == nums[i-1]:
                continue

            while left<right:
                s = nums[left] + nums[i] + nums[right]
                if s == 0:
                    solutions.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                if s>0:
                    right -= 1
                if s<0:
                    left += 1

        return solutions

                
        
            



                
