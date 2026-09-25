# type checking 

'''
a = 10
b = 15.5
c = 'Hi'
d = [1,2,34,5.6]
e = (1,2,3,4,5,6)
f = {'nam':"bob"}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,tuple))
print(isinstance(f,dict))

'''
'''
a = 'hi'
if isinstance(a, (int, dict)):
    print('WOHOO')
else:
    print('VIHOO')
'''

# checkimg if object belongs to its class or no

'''
class A:
    pass
class B(A):
    pass
b = B()
print(isinstance(b, A))
print(isinstance(b, B))
'''

# How they ask in interviews
'''
class A:
    pass
class B(A):
    pass
b = B()
print(type(b)==A)
print(type(b)==B)
print(isinstance(b,A))
print(isinstance(b,B))
'''

