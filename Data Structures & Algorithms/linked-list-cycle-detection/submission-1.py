# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        current = head

        while current is not None:
            if current.next == slow:
                return True
            if current.next is None:
                return False
            current = current.next.next
            slow = slow.next

        
        return False
