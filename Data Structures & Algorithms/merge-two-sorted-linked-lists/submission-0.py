# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            if l1 != None and l2 == None:
                while l1 != None:
                    head.next = l1
                    l1 = l1.next
                    head = head.next
            elif l2 != None and l1 == None:
                while l2 != None:
                    head.next = l2
                    l2 = l2.next
                    head = head.next
        return curr.next