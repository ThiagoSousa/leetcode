# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node, parent):
            if node is None:
                return parent

            new_head = dfs(node.next, node)
            node.next = parent
            return new_head

        return dfs(head, None)