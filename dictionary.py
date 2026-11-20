#Part A

student = {"name": "Aarav", "age": 20, "city": "Vadodara", "course": "B.Tech", "cgpa": 8.4}

print(student)
print("keys:", len(student))
print(student["name"])
print(student.get("cgpa"))
print(student.get("email"))
#print(student["email"])
# KeyError: 'email', becuase the key doesn't exist.
print("Keys:", student.keys())
print("Values:", student.values())
print("Key values:", student.items())

#Part B

student = {"name": "Aarav", "age": 20, "city": "Vadodara", "course": "B.Tech", "cgpa": 8.4}

student["email"] = "aarav123@gmail.com"
print(student)
student["cgpa"] = 8.9
print(student)
student.update({"semester": 5,"hostel": "Yes"})
print(student)
removed = student.pop("hostel")
print(removed)
del student["city"]
popping = student.popitem()
print(popping)
if"course" in student:
   print("It does")
else:
   print("It does not")

#Part C

student = {"name": "Aarav", "age": 20, "city": "Vadodara", "course": "B.Tech", "cgpa": 8.4}

for key, value in student.items():
    print(key, ":", value)

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

college = {"student1": {"name": "Aarav", "cgpa": 8.4}, "student2": {"name": "Priya", "cgpa": 9.1}}

for student, details in college.items():
    print("NAME:", details["name"])
    print("CGPA:", details["cgpa"])

squares = {x:x**2 for x in range(1,6)}
print(squares)

student = {"name": "Aarav", "age": 20, "city": "Vadodara", "course": "B.Tech", "cgpa": 8.4}

scp = student.copy()
scp["name"] = "Shasad"
print("OG:", student)
print("COPY:", scp)

#Part D

subjects = ["Maths", "Physics", "Chemistry", "English"]
marks = [88, 76, 92, 81]
combo = dict(zip(subjects, marks))
print(combo)

sentence = "the quick brown fox jumps over the lazy dog the fox runs"
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)

marks_dict = {"Aarav": 78, "Priya": 92, "Rohan": 45, "Meera": 88}
highest = max(marks_dict, key=marks_dict.get)
lowest = min(marks_dict, key=marks_dict.get)
average = sum(marks_dict.values()) /4
print("HIGHEST:", highest)
print("LOWEST:", lowest)
print("AVG.:", average)






