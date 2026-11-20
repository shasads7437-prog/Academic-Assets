#Part A
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Pune", "Hyderabad", "Jaipur"]
print(cities)
print(len(cities))
print(cities[0])
print(cities[3])
print(cities[0:3:1])
print(cities[2:6:1])

#Part B
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Pune", "Hyderabad", "Jaipur"]
print(cities[-1])
print(cities[-2])
print(cities[-3::])
print(cities[1]+cities[-1])
print(cities[::-1])

#Part C
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Pune", "Hyderabad", "Jaipur"]
cities.append("Ahmedabad")
print(cities)
cities.insert(2, "Surat")
print(cities)
#Rest is on next
cities.extend(["Indore", "Shilong", "Lucknow"])
print(cities)
cities.remove("Pune")
print(cities)
del cities[2]
print(cities)
#Rest is on next
luck=cities.pop()
print(luck)
print(cities)
cities.sort()
print(cities)


#Part D
marks = [78, 45, 89, 92, 34, 67, 55, 88]
print(max(marks))
print(min(marks))
print(sum(marks))
#Rest is on next
data = [["Aarav", 78], ["Priya", 92], ["Rohan", 45]]
print(f"{data[0][0]} scored {data[0][1]}marks")
print(f"{data[1][0]} scored {data[1][1]}marks")
print(f"{data[2][0]} scored {data[2][1]}marks")



