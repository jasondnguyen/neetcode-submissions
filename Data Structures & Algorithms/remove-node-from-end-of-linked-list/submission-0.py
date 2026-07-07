# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        current = head

        while current:
            total_length += 1
            current = current.next
        
        target_i = total_length - n

        if target_i == 0:
            return head.next
        else:
            prev = None
            current = head
            index = 0

            while index != target_i:
                prev = current
                current = current.next
                index += 1
            
            prev.next = current.next

        
        return head
    
    