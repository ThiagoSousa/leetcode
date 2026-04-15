# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        self.head = head
        def is_palindrome(node):

            if node is None:
                return True

            result = is_palindrome(node.next) and node.val==self.head.val
            self.head = self.head.next
            return result
            
        return is_palindrome(head)