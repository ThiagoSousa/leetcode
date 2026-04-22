class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))
        for i in range(3):
            max_index = distinct_nums.index(max(distinct_nums))
            item = distinct_nums.pop(max_index)
            if len(distinct_nums) == 0 and i!=2:
                return max(nums)
        return item

        # nums = sorted(nums, reverse=True)
        # if len(nums)<3:
        #     return nums[0]
        # return nums[2]
