# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == None or  head.next == None:
            return head
        now = head
        next = head.next
        pre = None
        while next is not None :
            now.next = pre
            pre = now
            now = next
            next = next.next
        now.next = pre
        head = now
        return head
        