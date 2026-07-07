# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        reverse = prev
        forward = head
        current = head

        while forward and reverse:
            if forward == reverse:
                break
            forward = forward.next
            current.next = reverse
            current = current.next

            reverse = reverse.next
            current.next = forward
            current = current.next
        
        current.next = None
        
        return head

            