class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right):

            # print(left, right)

            # stop conditions
            if right<=left:
                if target>nums[left]:
                    return left+1
                else:
                    return left

            middle = left+int((right-left)/2)

            if target==nums[middle]:
                return middle
            
            if target>nums[middle]:
                return binary_search(middle+1, right)
            elif target<nums[middle]:
                return binary_search(left, middle-1)
        
        return binary_search(0, len(nums)-1)