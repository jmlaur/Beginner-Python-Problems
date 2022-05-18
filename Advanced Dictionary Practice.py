
#1-4 dictionary

friends = {
    "Bob":"Birmingham",
    "Joe":"Ann Arbor",
    "Thomas":"New York City",
    "Kyle":"Los Angeles",
    "Allen":"Detroit"
}

#1

print(friends)

#2

location = friends.get("Kyle", "Does not exist")
print(location)
location = friends.get("A", "Does not exist")
print(location)

#3

for key, value in friends.items():
    print(key, " lives in ", value)

#4

for key in friends.keys():
    print(key)

for value in friends.values():
    print(value)



#5
rivers = {
    "Mississippi River":"United States",
    "Nile River":"Egypt",
    "Amazon River":"Peru"
}

for key, value in rivers.items():
    print(key, "runs through ", value)

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)




#6

phone = {
    "Bob":"2483432345",
    "Joe":"2483965678",
    "Thomas":"2482814589",
    "Kyle":"2486542389",
    "Allen":"2486789843"
}

name = input("Name: ")

while True:
    for x in phone.keys():
        if name == x:
            print(phone[x])
            break;
        else:
            new = input("Enter a phone number: ")
            new1 = { name:new }
            print(phone)
            break;
    break;

