#1

def sum(x, y):
    z = x + y
    return z


num1 = int(input())
num2 = int(input())
print(sum(num1, num2))


#2

def show_employee(n, s=9000):
    print("Name:", n)
    print("Salary:", s)


show_employee("Bob")
show_employee("Kyle", 12000)
