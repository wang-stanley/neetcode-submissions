# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        r = head
        l = None
        
        while r:
            r = r.next
            if l:
                l = l.next

            count += 1

            if count == n + 1:
                l = head

        # print("l:", l.val)
        # print("r:", r.val)
        
        if not l:
            return head.next

        l.next = l.next.next
        return head