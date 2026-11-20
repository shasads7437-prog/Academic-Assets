#PartA

for n in range(1,11,1):
    print(n, end=" ")
print()

for m in range(2,21,2):
    print(m, end=" ")
print()

# A1 comp

for v in range(1,11,1):
    print(v, v**2)

fruits = ["Apple", "Banana", "Mango", "Grapes"] 
for fruit in  fruits:
    print(fruit)

j = 0
for i in range (1,51,1):
    j = j+i
print("Sum of all:", j)

wood = "Acacia"
rev = ""
for ch in wood:
    rev = ch + rev
print("Reversed:", rev)
num = [22,33,44,88,100]
maximum = num[0]
minimum = num[0]
for q in num:
    if q > maximum:
        maximum = q
    if n < minimum:
       minimum = q
print("Max=", maximum)
print("Min=", minimum)

#A4 comp

names = ["Krish", "Ranbir", "Jaskirat", "Shasad", "Ansh"]
for w in names:
    if len(w)>5:
        print(w)
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ = 0
for g in numb:
    if g%2!=0:
        summ = summ + g
print("Odd sum=", summ)
 
#A5 comp

#Part B

k = 10
while k>=1:
    print(k)
    k = k - 1

#B1 comp

l = 1
while l<=20:
    print(l)
    l = l + 2

#B2 comp 

f = int(input("Enter number:"))
o = 1
equal = 0
while o<=f:
    equal = equal + o
    o = o + 1
print("Addition=", equal)

#B3 comp 

u = int(input("Enter number:"))
y = 1
while y<=10:
    print(u, "x",y,"=",u*y)
    y = y + 1

#B4 comp 

t = int(input("Enter number:"))
count = 0 
while t>0:
    t = t//10
    count = count + 1
print("Digits:", count)

#B5 comp 

n = int(input("Enter digit:"))
steps = 0
while n!=1:
    print(n, end=" ")
    if n%2==0:
        n = n//2
    else:
        n = 3*n + 1
    steps = steps + 1
print(1)
print("Steps:", steps)
 
#Part C

a = int(input("Enter input:"))
for r in range(1, a+1):
    for e in range(1, r+1):
        print(e, end="")
    print()

s = int(input("Enter rows:"))
for d in range (s, 0, -1):
    for h in range(d):
        print("*",end="")
    print()

b = int(input("Enter rows:"))
for v in range(1, b+1):
    for u in range (b-1):
       print("",end="")
    for z in range(v):
        print("*", end="")
    print()

r = int(input("Enter rows:"))
num = 1
for k in range(1, r+1):
    for l in range(1, k+1):
        print(num, end="")
        num = num + 1
    print()

    #C1 comp

n = int(input("Enter number:"))
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
    print("Reversed:", rev)

    #C2 comp


j = int(input("Enter input:"))
if j<2:
    print("Not prime")
else:
    for i in range(2,j):
        if j%i==0:
            print("Not prime")
            break
        else:
            print("Prime")

#C3 comp 

n = int(input("Enter number:"))
print("Factors:")
for i in range(1, n+1):
    if n%i==0:
        print(i)

for i in range(1,21):
    if i%3==0:
        continue
    print(i, end=" ")
print()

#C5 comp

#Part D

n = int(input("Enter number:"))
temp = n
digits = len(str(n))
sum = 0
while temp>0:
    digit = temp%10
    sum = sum + digit**digits
    temp = temp//10
if sum == n:
    print("Armstrong number")
else:
    print("Not")

#D1 comp

for i in range(1, 6):
    print("Table of", i)
    for j in range (1, 11):
        print(i, "x", j, "=", i*j)
    print()

#D2 comp

n = int(input("Enter series:"))
a = 0
b = 1
count = 0
while count<n:
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    count = count + 1

#Part D comp