# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if root is None:
            return []

        all_paths = []
        
        def dfs(node, path):

            if node.left is None and node.right is None:
                if sum(path)+node.val == targetSum:
                    all_paths.append(path+[node.val])
                return
            if node.left is not None:
                dfs(node.left, path+[node.val])
            if node.right is not None:
                dfs(node.right, path+[node.val])

        dfs(root, [])

        return all_paths