class circular_queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * self.size

    def enqueue(self, val):
        # Queue is full
        if self.front == (self.rear + 1) % self.size:
            return 'Queue is full'
        # Queue is empty
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val

    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            return 'Queue is empty'

        val = self.q[self.front]

        # Only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return val

    def display(self):
        # Queue is empty
        if self.front == -1:
            return 'Queue is empty'

        i = self.front

        while True:
            print(self.q[i], end=' ')

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


cq = circular_queue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

print(cq.dequeue())
print(cq.dequeue())

cq.enqueue(50)
cq.enqueue(60)

cq.display()     
















        
   