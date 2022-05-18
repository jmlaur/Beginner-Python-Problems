#1

num = 0
while num >= 0:
    num = int(input("Input a number: "))
    if num >= 0:
        print(num)


#2

password = input("Make a password: ")
test = ''
while test != password:
    test = input("Password: ")
    if test == password:
        print("Correct!")
    else:
        print("Incorrect!")
   

#3

x = []
count = 0
while count < 10:
    num = int(input("Input a number: "))
    x.append(num)
    count += 1
    print("Count:", count)

print("Largest:", max(x))
print("Smallest:", min(x))


#4

positive = []
negative = []
num = 1
while num != 0:
    num = int(input("Input a number: "))
    if num != 0:
        print(num)
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        print(0);

print("Positive:", *positive, sep = ', ')


#5
i = 0
python = ["P", "y", "t", "h", "o", "n", "a"]
while python[i] != python[6]:
    print(python[i])
    i += 1
