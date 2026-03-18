# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        remainder = 0
        result = []
        while l1 is not None or l2 is not None:
            op1 = 0
            if l1 is not None:
                op1 = l1.val
                l1 = l1.next

            op2 = 0
            if l2 is not None:
                op2 = l2.val
                l2 = l2.next

            s = op1 + op2 + remainder
            remainder = int(s/10)
            s = s%10

            result.append(ListNode(val=s))

        if remainder>0:
            result.append(ListNode(val=remainder))

        for i in range(len(result)-1):
            result[i].next = result[i+1]

        return result[0]

            

            
        