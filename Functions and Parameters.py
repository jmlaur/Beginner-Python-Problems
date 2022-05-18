#1

def triple(x):
    num = x*3
    print(num)

triple(3)
triple(4)


#2

def triangleArea(b, h):
    a = (b*h)//2
    print(a)

triangleArea(5, 6)


#3

def calculate_area(side_length=10):
    a = side_length*side_length
    print("The area of a square with sides of length", side_length, "is", a)

s = int(input("Enter side length: "))
if s <= 0:
    calculate_area()
else:
    calculate_area(s)
