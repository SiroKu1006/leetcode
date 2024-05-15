# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: ListNode) ->ListNode:
        # s = ""
        # while head.next != None:
        #     s+= str(head.val)
        #     head =head.next
        # s+= str(head.val)
        # s = str(int(s)*2)
        # ans_list = ListNode()
        # head = ans_list
        # for i in range(len(s)-1):
        #     ans_list.val = int(s[i])
        #     ans_list.next = ListNode()
        #     ans_list = ans_list.next
        # ans_list.val = int(s[-1])
        # ans_list.next = None
        # return head

        prev = None
        while head :
            nex  = head.next
            head.next = prev
            prev = head
            head = nex
        c = 0
        cas = prev
        while prev.next is not None:
            k = prev.val*2+c
            prev.val = k%10
            c = k//10
            prev = prev.next
        k = prev.val*2+c
        prev.val = k%10
        c = k//10
        if c!= 0:
            prev.next = ListNode()
            prev = prev.next
            prev.val = c
            prev.next = None
        ans = None
        while cas:
            nex = cas.next
            cas.next = ans
            ans = cas
            cas = nex

        return ans
