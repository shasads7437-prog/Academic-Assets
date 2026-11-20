#Part A (Set creation & operation)

fruits = {"Mango", "Apple", "Banana", "Grapes", "Papaya", "Orange", "Guava"}

print(fruits)
print(len(fruits))

basket = {"Apple", "Mango", "Apple", "Kiwi", "Mango"} 
print(basket)
#Duplication is not allowed in set.

#print(fruits[0])
#TypeError: 'set' object is not subscriptable

print("Mango" in fruits)
print("Kiwi" in fruits)

flist = list(fruits)
print(flist)
fruits2 = set(flist)
print(fruits2)

#Part B

fruits.add("Kiwi")
print(fruits)
fruits.update(["Litchi","Pomegranate","Fig"])
print(fruits)
fruits.remove("Papaya")
print(fruits)
#switch
fruits.discard("Watermelon")
print(fruits)
#fruits.remove("Watermelon")
#print(fruits)
# No error show when using discard, but whe we use remove, it raises a KeyError: 'Watermelon'
waste = fruits.pop()
print(waste)
print(fruits)
# Pop removes a random element from the set.
fruitsclc = fruits.copy()
fruitsclc.clear()
print(fruitsclc)

#Part C

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(setA|setB)
print(setA.union(setB))
print(setA & setB)                                                 
print(setA.intersection(setB))
print(setA-setB)
print(setA.difference(setB))
print(setB-setA)
print(setB.difference(setA))
print(setA^setB)
print(setA.symmetric_difference(setB))
print({1,2}.issubset(setA))
print(setA.issuperset({1,2}))
print(setA.isdisjoint(setB))
print(setA.isdisjoint({9,10}))

#Part D

chess = ["Aarav", "Priya", "Rohan", "Meera"]
robotics = ["Rohan", "Isha", "Meera", "Kabir"]
setc = set(chess)
setr = set(robotics)
print(setc & setr)
print(setc|setr)
print(setc-setr)
scores = [67, 89, 45, 67, 89, 92, 45, 78]
sets = set(scores)
print(sets)
square = {number**2 for number in range(1,11)}
print(square)