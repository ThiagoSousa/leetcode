# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                    node = head
                else:
                    node.next = list1
                    node = node.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    node = head
                else:
                    node.next = list2
                    node = node.next
                list2 = list2.next

        if list1:
            if head is None:
                head = list1
            else:
                node.next = list1
        
        if list2:
            if head is None:
                head = list2
            else:
                node.next = list2

        # while list1 is not None:
        #     if head is None:
        #         head = list1
        #         node = head
        #     else:
        #         node.next = list1
        #         node = node.next
        #     list1 = list1.next

        # while list2 is not None:
        #     if head is None:
        #         head = list2
        #         node = head
        #     else:
        #         node.next = list2
        #         node = node.next
        #     list2 = list2.next

        return head
        