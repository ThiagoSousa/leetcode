# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = []
        def dfs(node, path):

            if node.right is None and node.left is None:
                paths.append(path+[node.val])

            if node.left is not None:
                dfs(node.left, path+[node.val])

            if node.right is not None:
                dfs(node.right, path+[node.val])

        dfs(root, [])

        paths = ["->".join([str(i) for i in path]) for path in paths]

        return paths