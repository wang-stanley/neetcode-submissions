# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = cur = ListNode()

        while l1 or l2 or carry:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val

            placeSum = val1 + val2 + carry
            carry = placeSum // 10
            placeSum %= 10

            cur.next = ListNode(placeSum, None)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next