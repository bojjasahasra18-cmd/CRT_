class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node 

def deletion_begin(head):
    if head is None:
        print("Error")
        return
    new_head=head.next
    del head
    return new_head

def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    return head
def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None 
    curr=head
    while curr.next.next:
        curr=curr.next
    del_node=curr.next
    curr.next=None
    return head

def insert_at_position(node,data):
    if node is None or node.next is None:
        print("Error")
        return node
    new_node=Node(data)
    new_node.next=node.next
    node.next=new_node
    return node

def deletion_at_position(node):
    if node is None or node.next is None:
        print("Error")
        return 
    new_node = node.next
    node.next = new_node.next
    del new_node
    return node

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)

print("Insertion at the begin")
traverse(head)

print("Insertion at the end")
head=insert_end(head,40)
traverse(head)

print("Insertion at position")
head=insert_at_position(head,25)
traverse(head)

print("Deletion at the begin")
head = deletion_begin(head)
traverse(head)

print("Deletion at the end")
head = deletion_end(head)
traverse(head)

print("Deletion at position")
head = deletion_at_position(head)
traverse(head)