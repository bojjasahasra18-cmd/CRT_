# 24/09/2026
'''
Insert at beggining

1. new_node
2. if Head is None:
    head = new_node
3. else:
    new_node.next = head
    head.prev = new_node
    head = new_node
'''

'''
insert at end

1. new_node
2. if head is None:
    head = new_node
3. else:
    curr = head
    while curr:
        curr.next = new_node
        new_node.prev = curr
        curr = curr.next
'''



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

# insert at the beggining
 
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
# insert at the end

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr= curr.next
        new_node.prev = curr
        curr.next = new_node
        curr = new_node

# deletion at the beggining

    def delete_at_start(self):
        if self.head is None:
            print('ERRORRRRRR')
            return
        old_head = self.head
        self.head = old_head.next
        if self.head is not None:
            self.head.prev = None
        old_head.next = None
# deletion at the end

    def delete_at_end(self):
        if self.head is None:
            print('ERRORRRR')
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next

        del_node = curr.next
        curr.next = None
        del_node.prev = None

# counting no of nodes in the linked list

    def count_nodes(self):
        count = 0
        if self.head is None:
            return 0
        curr=self.head
        while curr.next:
            count +=1
            curr = curr.next
        a = count+1
        return a

    def delete_at_pos(self, pos):
        if self.head is None or pos < 0:
            print('ERROR')
            return
        if pos == 0:
            self.delete_at_start()
            return

        curr = self.head
        for _ in range(pos):
            if curr is None:
                print('ERROR')
                return
            curr = curr.next

        if curr is None:
            print('ERROR')
            return
        curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev



# Traversal

    def Traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end = '<-->')
            curr = curr.next
        print('None')

dll = DoublyLinkedList()
dll.insert_at_start(10)
dll.insert_at_start(30)
dll.insert_at_start(20)
dll.Traverse()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.Traverse()
dll.delete_at_start()
dll.Traverse()
dll.delete_at_end()
dll.Traverse()
print(dll.count_nodes())



