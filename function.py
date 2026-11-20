#Part A

def greet():
    print("Hello, Welcome to python!")

greet()

def greet_user(name):
    print("Hello", name)
name = "Sir"
greet_user(name)

a = 11
b = 10
def sum(a,b):
    print(a+b)
sum(a,b)

n = int(input("Enter num:"))
def prop(n):
    if n%2 == 0:
       print("even")
prop(n)

def square():
    for s in range(1 , 11):
        print(s**2)
square()