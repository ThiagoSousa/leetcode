class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = float("inf")

        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if (i>0 and nums[i]==nums[i-1]):
                continue

            while left<right:
                s = nums[left] + nums[i] + nums[right]
                if abs(s-target)<abs(best-target):
                    best = s
                    if abs(s-target) == 0:
                        return best
                    # while left<right and nums[left] == nums[left-1]:
                    #     left += 1
                if s>target:
                    right -=1
                elif s<target:
                    left += 1
        return best