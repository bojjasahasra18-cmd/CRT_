# 23/09/2026

'''
Doubly Linked List

data stores nodes
Node -> 3parts: data, next, prev

'''
'''
Algorithm:
1.Create Nodes
2.Insert Data
3. Connection between nodes
4. Traverse the list
'''


'''
# Creating node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(10)
node2 = Node(30)
node3 = Node(20)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2


# Forward Traversal

def Traverse():
    curr = node1
    while curr:
        print(curr.data, end = '<-->')
        curr = curr.next
    print('None')
Traverse()

# Backward Traversal

def Traverse(head):
    curr = head
    while curr:
        print(curr.data, end = '<-->')
        curr = curr.prev
    print('None')
Traverse(head=node3)
'''
'''
# Insert a node at the beginning 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_at_start(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def Traverse(head):
    curr = head
    while curr:
        print(curr.data, end = '<-->')
        curr = curr.next
    print('None')
head = None
head = insert_at_start(head, 10)
head = insert_at_start(head, 30)
head = insert_at_start(head, 20)
Traverse(head)
'''
'''

# Insert a node at the end

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head

def Traverse(head):
    curr = head
    while curr:
        print(curr.data, end = '<-->')
        curr = curr.next
    print('None')

head = None
head = insert_at_end(head, 10)
head = insert_at_end(head, 30)
head = insert_at_end(head, 20)
Traverse(head)

'''
'''
# insert a node at after a given code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_after(node, data):
    if node is None:
        print('Error')
        return

    new_node = Node(data)
    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node


def Traverse(head):
    curr = head
    while curr:
        print(curr.data, end='<-->')
        curr = curr.next
    print('None')


head = Node(10)
node2 = Node(20)
node3 = Node(30)

head.next = node2
node2.prev = head

node2.next = node3
node3.prev = node2

insert_after(node2, 25)

Traverse(head)
'''

'''

# insert the node before a given node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_before(node, data):
    if node is None:
        print('Error')
        return

    new_node = Node(data)

    new_node.prev = node.prev
    new_node.next = node

    if node.prev:
        node.prev.next = new_node

    node.prev = new_node


def Traverse(head):
    curr = head
    while curr:
        print(curr.data, end='<-->')
        curr = curr.next
    print('None')


head = Node(10)
node2 = Node(20)
node3 = Node(30)

head.next = node2
node2.prev = head

node2.next = node3
node3.prev = node2

insert_before(node2, 15)

Traverse(head)
'''


