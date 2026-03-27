# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        head = ListNode()
        node = head
        last = None

        while True:
            min_val = float("inf")
            min_index = -1
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            
            if min_index == -1:
                if last is None:
                    return None
                last.next = None
                return head

            node.val = min_val
            node.next = ListNode()
            last = node
            node = node.next
            lists[min_index] = lists[min_index].next



