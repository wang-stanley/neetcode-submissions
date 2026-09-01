# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        curIdx = 0

        while curIdx < left - 1:
            dummy = dummy.next
            curIdx += 1
        
        # Now, curIdx == (left - 1), the previous node for the future reversed sublist

        prev = dummy
        cur = dummy.next
        tmp = cur.next

        while curIdx < right:
            cur.next = prev
            prev = cur
            cur = tmp
            if cur:
                tmp = cur.next
            curIdx += 1

        dummy.next.next = cur
        dummy.next = prev
        
        if left == 1:
            return prev
        return head