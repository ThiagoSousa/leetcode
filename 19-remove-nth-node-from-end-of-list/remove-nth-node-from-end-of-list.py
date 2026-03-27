# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        
        position = count-n
        
        print(position, count)
        if position == 0:
            return head.next

        node = head
        count = 0
        while count<position-1:
            count += 1
            node = node.next
        if node.next is not None:
            node.next = node.next.next
        else:
            return None

        return head

