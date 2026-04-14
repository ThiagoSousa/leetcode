class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        left = 0
        right = 1
        output = []
        while right<len(nums):

            while right<len(nums) and nums[right]==nums[right-1]+1:
                right += 1

            if right-left==1:
                output.append(str(nums[left]))
            else:
                output.append("{0}->{1}".format(nums[left], nums[right-1]))
            left = right
            right += 1

        if left<len(nums):
            output.append(str(nums[left]))

        return output