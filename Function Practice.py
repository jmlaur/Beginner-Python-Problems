#1
def add(num1, num2):
    num = num1 + num2
    print(num1, "+", num2, "=", num)

def subtract(num1, num2):
    num = num1 - num2
    print(num1, "-", num2, "=", num)

def divide(num1, num2):
    num = num1 / num2
    print(num1, "/", num2, "=", num)

def multiply(num1, num2):
    num = num1*num2
    print(num1, "*", num2, "=", num)

num1 = int(input("Num1 :"))
num2 = int(input("Num2 :"))
operator_ = input("Would you like to add, subtract, divide, or multiply these numbers?: ")
if operator_.lower() == "add":
    add(num1, num2)
elif operator_.lower() == "subtract":
    subtract(num1, num2)
elif operator_.lower() == "divide":
    divide(num1, num2)
elif operator_.lower() == "multiply":
    multiply(num1, num2)
else:
    print("Invalid operator chosen!")

#2
def evenOrOdd(even_or_odd):
    if even_or_odd % 2 == 0:
        print("Even")
    elif even_or_odd % 2 > 0:
        print("Odd")

even_or_odd = int(input("Input a number to determine if it is even or odd: "))
evenOrOdd(even_or_odd)

#3
def uppercase(word):
    print(word.upper())

word = input("Enter a word: ")
uppercase(word)


