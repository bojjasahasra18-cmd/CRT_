'''
# operations: enqueue, dequeue, peek
# front, rear pointers
front +=1 -when dequeue happens
rear +=1 -when enqueue happens
# FIFO - first in first out

'''


class Queue:
    def __init__(self):
        self.s = []
    def enqueue(self, val):
        self.s.append(val)
    def is_empty(self):
        return len(self.s)==0
    def dequeue(self,val):
        if self.is_empty():
            return 'Stack is empty'
        return self.s.pop(val)
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.s[0]
    def size(self):
        return len(self.s)

qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.dequeue(1)
print(qu.peek())
qu.dequeue(0)
print(qu.dequeue(0))
print(qu.size())


