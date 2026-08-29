# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        cur1, cur2 = l1, l2
        tail = ListNode(0, l1)

        while cur1:
            a, b = cur1.val, 0
            if cur2:
                b = cur2.val
                cur2 = cur2.next

            placeSum = a + b

            if carry:
                placeSum += 1

            if placeSum >= 10:
                carry = True
                placeSum %= 10
            else:
                carry = False

            cur1.val = placeSum
            cur1 = cur1.next
            tail = tail.next

        while cur2:
            tail.next = cur2

            if carry:
                cur2.val += 1

                if cur2.val >= 10:
                    carry = True
                    cur2.val %= 10
                else:
                    carry = False

            tail = tail.next
            cur2 = cur2.next

        if not cur1 and not cur2 and carry:
            tail.next = ListNode(1, None)
            return l1

        return l1