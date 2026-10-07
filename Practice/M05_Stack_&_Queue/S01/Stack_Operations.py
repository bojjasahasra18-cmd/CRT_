'''
# operation: push, pop
# top is a pointer used to point the top-most element of the stack
top +=1 (when pushing an element)
top -= 1 (when popping an element)
# time complexity
O(1) -for each operation

'''

'''
# implementation of stack
class Stack:
    def __init__(self):
        self.s=[]
    def push(self, val):
        self.s.append(val)
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.s.pop()
    
    def is_empty(self):
       return len(self.s)==0
    def size(self):
        return len(self.s)
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.s[-1]
    

st = Stack()
st.push(10)
st.push(20)
st.pop
st.push(1000)
st.pop()
st.pop()
st.push(10000)
st.push(10)
st.push(30)
st.push(68)
print(st.is_empty())
print(st.peek())
st.pop()
print(st.peek())

'''
'''
# implementation of stack using top variable

class Stack_top:
    def  __init__(self, size):
        self.size = size
        self.top = -1
        self.s = [None]*self.size
    def push(self,val):
        if self.top == self.size -1:
            return 'Stack is full'
        self.top += 1
        self.s[self.top] = val
    def is_empty(self):
        return self.top == -1
    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        val = self.s[self.top]
        self.top -= 1
        return val
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.s[self.top]
    def sizee(self):
        return self.top+1

st = Stack_top(5)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
print(st.push(70))
st.pop()
st.pop()
st.pop()
print(st.peek())
print(st.sizee())

'''

# stack implementation using sll
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.top = None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    # def is_empty():
    #     return self.top == -1
    
    def pop(self):
        if self.top is None:
            return 'Stack is empty'
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return 'Stack is empty'
        return self.top.data
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end = ' ->')
            temp = temp.next
        print('None')

st = sll()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.pop()
st.pop()
print(st.pop())
print(st.peek())
st.display()


    

