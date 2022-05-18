
#1
x = 0
for i in range(20):
    x += 1
    print(x)

#2
for i in range(0, 1000, 100):
    print(i)

#3
pizza = ["Cheese", "Pepperoni", "Spinach"]
for i in range(len(pizza)):
    print(pizza[i])

#4
b = 0
num = int(input("How many numbers do you want to total?: "))
for i in range(num):
    y = int(input("Enter a number: "))
    b += y
print("Sum: ", b)



#Extra Challenge
my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even = []
not_even = []
outlier = []
for i in range(len(my_list)):
    if (my_list[i] % 2 > 0):
        not_even.append(my_list[i])
    elif (my_list[i] % 2 == 0):
        even.append(my_list[i])
    else:
        outlier.append(my_list[i])
print("Not even: ", not_even)
print("Even: ", even)
print("Outlier: ", outlier)
        
