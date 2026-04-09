# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sum):
            if node is None:
                return False

            if node.left is None and node.right is None:
                if sum+node.val == targetSum:
                    return True
                return False

            return dfs(node.left, sum+node.val) or dfs(node.right, sum+node.val)

        return dfs(root, 0)