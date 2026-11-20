#Part A (Positive indexing)

students = ("Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha", "Vikram", "Diya")

print(students)
print(len(students))
print(students[0])
print(students[3])
print(students[0:3:1])
print(students[1:6:1])

#Part B (Negative indexing)

students = ("Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha", "Vikram", "Diya")

print(students[-1])
print(students[-2])
print(students[-3::])
print(students[0] + students[-1])
print(students[::-1])

#Part C (Methods & Immutability)

students = ("Aarav", "Priya", "Rohan", "Meera", "Kabir", "Isha", "Vikram", "Diya")

print(students.count("Rohan"))
print(students.index("Kabir"))
#students[1]="Ananya"
 #TypeError: 'tuple' object does not support item assignment
student_list= list(students)
student_list.append("Ananya")
students= tuple(student_list)
print(students)
extras=("Neha", "Arjun")
students= students+extras
print(students)
result=("Pass", "Fail")*3
print(result)
print(sorted(students))

#Part D (Mixed)

marks = (78, 45, 89, 92, 34, 67, 55, 88)

print(max(marks))
print(min(marks))
print(sum(marks))

exam_data = (("Aarav", 78), ("Priya", 92), ("Rohan", 45))

print(f"{exam_data[0][0]} scored {exam_data[0][1]} marks")
print(f"{exam_data[1][0]} scored {exam_data[1][1]} marks")
print(f"{exam_data[2][0]} scored {exam_data[2][1]} marks")

#data=("Python", "Tuples", 2026) 
subject, topic, year=("Python", "Tuples", 2026) 
print(subject)
print(topic)
print(year)