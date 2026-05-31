# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def halfLL(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
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

        mid = halfLL(head)

        l2 = mid.next      # start second half
        mid.next = None    # split list

        l2 = reverse(l2)

        curr = head
        while curr and l2:
            nxt1 = curr.next
            nxt2 = l2.next

            curr.next = l2
            l2.next = nxt1

            curr = nxt1
            l2 = nxt2