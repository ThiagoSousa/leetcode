# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, height) -> int:

            if node is None:
                return height
            
            left_height = dfs(node.left, height+1)
            if left_height < 0:
                return left_height
            right_height = dfs(node.right, height+1)
            if right_height < 0:
                return right_height

            if abs(left_height-right_height)<=1:
                return max(left_height, right_height)
            return -1

        valid = dfs(root, 0)

        if valid<0:
            return False
        return True

            