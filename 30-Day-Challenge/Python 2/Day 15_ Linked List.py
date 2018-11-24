class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
## Recursive solution
    def insert(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head

## Not recursive
    def insert(self,head,data):
        nextnode = Node(data)
        if head == None:
            return nextnode
        else: 
            node = head
            while node.next != None:
                node = node.next
            node.next = nextnode
            return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
