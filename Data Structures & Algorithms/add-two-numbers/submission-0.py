# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(-1)
        curr = head
        while l1 or l2 or carry > 0:
            if l1 and l2:
                summation = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                summation = l2.val + carry
                l2 = l2.next
            elif l1 and not l2:
                summation = l1.val + carry
                l1 = l1.next
            elif not l1 and not l2 and carry > 0:
                summation = carry
            if summation >= 10:
                curr.next = ListNode(summation % 10)
                carry = summation // 10
            else:
                curr.next = ListNode(summation)
                carry = 0
            curr = curr.next
        return head.next

