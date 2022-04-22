# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        start, end = head, self.reverse(slow)
        while start and end:
            if start.val != end.val: return False
            start = start.next
            end = end.next
            
        return True
        
    def reverse(self, head: Optional[ListNode]):
        prev = None
        while head:
            next_element = head.next
            head.next = prev
            prev = head
            head = next_element

        return prev
 