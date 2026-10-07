'''
# 2 types: Monotonic increasing and monotonic decreasing

    1. Monotonic increasing:
    small --> large
    2. Monotonic decreasing
    large--> small

# if asked 'strictly greater / smaller' then have to include the operators >= or <=

'''
'''
# increasing | genearl pattern
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
stack  = []
for i in arr:
    while stack and stack[-1] > i:
        stack.pop()
    stack.append(i)
print(stack)

# decreasing | general pattern
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
stack = []
for i in arr:
    while stack and stack[-1] < i:
        stack.pop()
    stack.append(i)
print(stack)

'''

# next greater element
def NextGreaterElement(arr):
    n = len(arr)
    res = [0]*n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        res[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return res



arr = [4,12,5,3,1,2,5,3,1,2,4,6]
# output: [12,-1,6,5,2,5,6,4,2,4,6,-1]
print(NextGreaterElement(arr))







