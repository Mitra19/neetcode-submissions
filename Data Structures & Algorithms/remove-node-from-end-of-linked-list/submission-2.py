# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        if head.next and not head.next.next and n == 1:
            head.next = None
            return head
        def reverseLL(head):
            if not head:
                return None
            prev = head
            curr = prev.next
            head.next = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        l1 = reverseLL(head)
        count = 1
        curr = l1

        while count < n-1:
            curr = curr.next
            count+=1
        prv, nxt = curr, curr.next.next
        curr.next.next = None
        prv.next = nxt
        l1 = reverseLL(l1)
        return l1