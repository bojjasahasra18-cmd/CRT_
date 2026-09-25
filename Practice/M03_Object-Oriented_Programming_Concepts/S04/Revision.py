# python code of using all 5 types of inheritance
'''
class A:
    def show_a(self):
        print("Class A")

# Single inheritance
class B(A):
    def show_b(self):
        print("Class B")

# Multilevel inheritance
class C(B):
    def show_c(self):
        print("Class C")

# Hierarchical inheritance
class D(A):
    def show_d(self):
        print("Class D")

# Multiple inheritance
class E(B, D):
    def show_e(self):
        print("Class E")

# Hybrid inheritance
class F(C, E):
    def show_f(self):
        print("Class F")

obj = F()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()
obj.show_e()
obj.show_f()
'''

# python code for polymorphism(duck typing)
'''
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

def display(obj):
    obj.show()

a = A()
b = B()
display(a)
display(b)
'''