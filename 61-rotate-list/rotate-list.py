# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        final_node = None
        while node is not None:
            final_node = node
            node = node.next
            length += 1

        if length == 0:
            return None
        
        k %= length
        position = length-k

        node = head
        i = 1
        while i<position:
            node = node.next
            i += 1
        final_node.next = head
        head = node.next
        node.next = None
        return head