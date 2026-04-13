# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        parent = None
        node = head
        while node is not None:
            next_node = node.next
            node.next = parent
            parent = node
            node = next_node
        return parent
            
