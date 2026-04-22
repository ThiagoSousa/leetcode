# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        
        if len(nums) == 1:
            return TreeNode(val=nums[0], left=None, right=None)
        
        middle_index = int(len(nums)/2)
        left = self.sortedArrayToBST(nums[:middle_index])
        right = self.sortedArrayToBST(nums[middle_index+1:])
        
        return TreeNode(val=nums[middle_index], left=left, right=right)
            
            
        
        
        