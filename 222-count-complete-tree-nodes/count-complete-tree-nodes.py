# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        node = root
        height = 0
        while node is not None:
            node = node.left
            height += 1

        def dfs(node, h):

            if h == height and node is None:
                return 1
            if h == height and node is not None:
                return 0

            # print(node, h)
            
            if h < height:
                result = dfs(node.right, h+1)
                if result>0:
                    result += dfs(node.left, h + 1)
                # print(result)
                return result

        count = dfs(root, 1)
                
        print(height, count)
        return 2**height-1-count
            
            

        