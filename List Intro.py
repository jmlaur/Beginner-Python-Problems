classmates = ["Bob", "George", "Julie", "Mary", "Thomas"]
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[3])
print(classmates[4])


#2

classmates.append("Joe")
classmates[0] = "dropped"
classmates.insert(0, "Fred")
del classmates[0]

#3

classmates.sort()
print(len(classmates))
classmates.remove("Julie")


#4

loc = ["PlaceOne", "PlaceTwo", "PlaceThree", "PlaceFour", "PlaceFive"]
print(loc)
print(sorted(loc))
print(loc)
print(sorted(loc))
print(loc)
loc.reverse()
print(loc)
loc.reverse()
print(loc)
loc.sort()
print(loc)
loc.reverse()
print(loc)

#bonus

authors = []
for i in range(5):
    x = input("Name: ")
    authors.append(x)
print(sorted(authors))
