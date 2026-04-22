# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if node is None:
                return 0

            s = 0
            if node.left is not None and node.left.left is None and node.left.right is None:
                s = node.left.val

            s += dfs(node.left)
            s += dfs(node.right)

            return s

        return dfs(root)  
        