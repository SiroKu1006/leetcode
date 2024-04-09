# def Optional(list):




class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class tree:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            
        current_node.next = new_node
    
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1)