# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # want to first find the halfway point. This can be done using Floyd's Tortoise and Hare algorithm

        slow, fast = head, head

        # If there are even number of elements: [0, 1, 2(s), 3] (f)
        # at the end of the loop, slow is at the start of the second half

        # If there are odd number of elements: [0, 1, 2(s), 3, 4(f)]
        # at the end of the loop, slow is at the midpoint

        # Either way, slow will be the last element of the reordered list
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"slow: {slow.val}")

        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # prev is now the head of our reversed second half

        cur = head
        while cur and prev and cur.next:
            temp1, temp2 = cur.next, prev.next
            
            cur.next = prev
            cur = temp1
            prev.next = cur
            prev = temp2
