# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        numbers = []
        for l in lists:
            while l is not None:
                numbers.append(l.val)
                l = l.next
        
        if len(numbers) == 0:
            return None
            
        numbers.sort()

        head = ListNode(val=numbers[0])
        node = head
        for i in numbers[1:]:
            new = ListNode(val=i)
            node.next = new
            node = node.next

        return head








