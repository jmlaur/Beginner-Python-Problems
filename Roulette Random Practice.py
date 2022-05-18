import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")



print(names)

x = len(names)

y = random.randint(0, (x - 1))

print(names[y] + " is buying food today!") 







