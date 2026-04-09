# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        solution = float("inf")
        output = []

        def dfs(node, depth):

            if node is None:
                return

            if node.left is None and node.right is None:
                # solution = min(solution, depth)
                output.append(depth)
                return

            left_depth = dfs(node.left, depth+1)
            right_depth = dfs(node.right, depth+1)

            # return min(left_depth, right_depth)

        if root is None:
            return 0
        dfs(root, 1)

        return min(output)