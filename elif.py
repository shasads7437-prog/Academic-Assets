#Part A

num = int(input("Enter number:"))
if num>0:
   print("Positive")

age = int(input("Enter age:"))
if age>= 18:
   print("Eligible to vote")

num = int(input("Enter number:"))
if num%2 == 0:
   print("Even number")

marks = int(input("Enter marks:"))
if marks>= 40:
   print("Pass")

temp = float(input("Temperature in celcius:"))
if temp>35:
   print("Hot day")

#Part B

num = int(input("Enter number:"))
if num%2 == 0:
   print("Even number")
else:
    print("Odd number")

num = int(input("Enter number:"))
if num>0:
   print("Positive")
else:
    print("Negative")

age = int(input("Enter age:"))
if age>= 18:
   print("Eligible to vote")
else:
    print("Not eligible to vote")

year = int(input("Enter year:"))
if year%4 == 0:
   print("Leap year")
else:
    print("Not leap year")

num1 = int(input("First number:"))
num2 = int(input("Second number:"))
if num1>num2 :
   print("Greater is:", num1)
else:
    print("Greater is:", num2)

#Part C

marks = int(input("Enter marks:"))
if marks>=90:
   print("Grade A")
elif marks>=75:
   print("Grade B")
elif marks>=60:
   print("Grade B")
elif marks>=40:
   print("Grade B")
else:
    print("Fail")

num1 = int(input("First number:"))
num2 = int(input("Second number:"))
num3 = int(input("Third number:"))
if num1>=num2 and num1>=num3:
   print("Greatest is:", num1)
elif num2>=num1 and num2>=num3:
   print("Greatest is:", num2)
else:
   print("Greatest is:", num3)


alp = input("Enter alphabet:")
if alp=='a' or alp=='e' or alp=='i' or alp=='o' or alp=='u':
   print("Vowel")
elif alp.isalpha():
    print("Consonant")
else:
    print("Invalid") 


a = int(input("First side:"))
b = int(input("Second side:"))
c = int(input("Third side:"))
if a==b and b==c:
   print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


num = int(input("Enter number:"))
if num>=0:
   if num==0:
      print("Zero")
   else:
      print("Positive")
else:
      print("Negative")

#Part D

username = input("Enter username:")
password = input("Enter password:")
if username == "admin" and password == "1234":
   print("Login successful")
else:
   print("Invalid")

amount = float(input("Enter amount:"))
if amount>10000:
   discount = amount*0.20
elif amount>=5000:
   discount = amount*0.10
else:
     discount = 0
final = amount-discount
print("Discount:", discount)
print("Complete amount:", final)

d = int(input("Enter first angle:"))
e = int(input("Enter second angle:"))
f = int(input("Enter third angle:"))
if d+e+f==180:
   if a==90 or b==90 or c==90:
      print("Valid triangle")
      print("Right angled triangle")
   else:
       print("Valid triangle")
       print("Not right angled triangle")
else:
     print("Invalid triangle")

day = int(input("Enter day number:"))
if day==1:
   print("Monday")
elif day==2:
   print("Tuesday")
elif day==3:
   print("Wednesday")
elif day==4:
   print("Thursday")
elif day==5:
   print("Friday")
elif day==6:
   print("Saturday")
elif day==7:
   print("Sunday")
else:
   print("Invalid")
