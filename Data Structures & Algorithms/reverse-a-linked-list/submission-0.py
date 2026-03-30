# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        current = head
        prev = None

        # 1
        # 0 -> None
        # prev = 0 -> None
        while current is not None:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
        return prev
