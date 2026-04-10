# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        seen = {}

        while headA is not None:
            seen[headA] = None
            headA = headA.next

        while headB is not None:
            if headB in seen:
                return headB
            headB = headB.next
        return None