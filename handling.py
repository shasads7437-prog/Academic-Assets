# take a number as input and print whether it is even or odd using if-else.

# take a number as input and print whether it is positive or negative using if-else.

# take age as input and print "Eligible to vote" or "Not eligible to vote" using if-else.

# take a year as input and check whether it is a leap year or not using if-else.

# take two numbers as input and print the greater number using if-else. 


n = int(input("Enter number:"))

if n%2==0:
   print("Even")
else:
   print("Odd")


m = int(input("Enter number:"))

if m>0:
   print("Postive")
else:
   print("Negative")


a = int(input("Enter age:"))

if a>=18:
   print("Eligible to vote")
else:
   print("Not eligible to vote")


k = int(input("Enter year:"))

if k%4==0:
   print("Leap year")
else:
   print("Not a leap year")


h = int(input("Enter num1:"))
g = int(input("Enter num2:"))

if h>g:
   print("Num1 is greater")
else:
   print("Num2 is greater")