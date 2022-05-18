#1

dog = True
print("Do you have a dog?" , dog)

#2

height = int(input("How tall are you?"))
if height >= 60:
    print("You can ride the roller coaster");
else:
        print("You can not ride the roller coaster");

#3

    
num = int(input("Give a number"))

if (num % 2) > 0:
    print("The number is odd");
else:
    print("The number is even");

#4

password = "bob"

test = input("What is the password?")

if test == "bob":
    print("Correct!");
else:
    print("Incorrect!")

#5

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num2, " is greater than ", num1)
else:
    print("They are equal")

#extra challenge

number = input("Enter a three digit number: ")
if len(number) > 3:
    print("Your number is greater than 3 digits!")
elif len(number) == 3:
        print("Your number is 3 digits!")
elif len(number) < 3:
    print("Your number is less than 3 digits!")
