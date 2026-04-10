# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        while fast is not None and slow is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
            if fast is not None and slow is not None and fast == slow:
                return True
        return False