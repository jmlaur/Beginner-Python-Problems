#1
age = int(input("how old are you"))
if age >= 4 and age <= 18:
    print("cost is $25")
elif age < 4:
    print("free")
else:
    print("cost is $40")

#2
cost = 0
order = input("What would you like?\n'Small Pizza' - $15\n'Medium Pizza' - $20\n'Large Pizza' - $25")

if order.lower() == "small pizza":
    cost += 15
    smallExtras = input("Would you like any extras?\n'Pepperoni for Small Pizza' - $2\n'Extra cheese' - $1\nOr type 'Cancel' to cancel.")
    if smallExtras.lower() == "pepperoni for small pizza":
        cost += 2
    elif smallExtras.lower() == "extra cheese":
        cost += 1
    else:
        print("Cancelled.")

if order.lower() == "medium pizza":
    cost += 20
    mediumExtras = input("Would you like any extras?\n'Pepperoni for Medium Pizza' - $3\n'Extra cheese' - $1\nOr type 'Cancel' to cancel.")
    if mediumExtras.lower() == "pepperoni for medium pizza":
        cost += 3
    elif mediumExtras.lower() == "extra cheese":
        cost += 1
    else:
        print("Cancelled.")

if order.lower() == "large pizza":
    cost += 20
    largeExtras = input("Would you like any extras?\n'Pepperoni for Large Pizza' - $3\n'Extra cheese' - $1\nOr type 'Cancel' to cancel.")
    if largeExtras.lower() == "pepperoni for medium pizza":
        cost += 3
    elif largeExtras.lower() == "extra cheese":
        cost += 1
    else:
        print("Cancelled.") 

print("Your total cost is $", cost)


#3
score = 0
q1 = input("What color is the sky?")
q2 = input("When is Halloween?")
q3 = input("What color is the grinch?")
q4 = input("What color is grass?")
q5 = input("What color is a dandelion?")

if q1.lower() == "blue":
    score += 1
else:
    score += 0

if q2.lower() == "october 31st" or q2.lower() == "october 31":
    score += 1
else:
    score += 0

if q3.lower() == "green":
    score += 1
else:
    score += 0

if q4.lower() == "green":
    score += 1
else:
    score += 0

if q5.lower() == "yellow":
    score += 1
else:
    score += 0

if score == 5:
    print("A")
elif score == 4:
    print("B")
elif score == 3:
    print("C")
elif score == 2:
    print("D")
elif score == 1:
    print("F")


