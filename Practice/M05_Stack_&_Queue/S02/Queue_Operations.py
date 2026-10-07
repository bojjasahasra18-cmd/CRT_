'''
# Queue implementation using front and rear pointers
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [None] * self.size

    def enqueue(self, val):
        if self.rear == self.size - 1:
            return 'Queue is full'
        self.rear +=1
        if self.front == -1:
            self.front = 0
        self.queue[self.rear] = val

    def dequeue(self):
        if self.front == -1:
            return 'Queue is empty'
        self.front +=1
        val = self.queue[self.front]
        return val

    def display(self):
        if self.front == -1:
            return 'Queue is empty'
        for i in range(self.front,self.rear+1):
            print(self.queue[i], end = ' ')
        print()

qu = Queue(10)
qu.enqueue(10)
qu.enqueue(19)
qu.enqueue(18)
qu.dequeue()
qu.display()

'''
# queue implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_ll:
    def __init__(self):
        self.front = -1
        self.rear = -1

    def enqueue(self, val):
        new_node = Node(val)
        if self.front == -1:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front == -1:
            return 'Queue is empty'
        val = self.front.data
        self.front = self.front.next
        if self.front == -1:
            self.rear = -1
        return val
    def display(self):
        if self.front == -1:
            return 'Queue is empty'
        temp = self.front
        while temp:
            print(temp.data, end = '->')
            temp = temp.next
        print()

qu = Queue_ll()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.dequeue()
qu.enqueue(40)
qu.display()
