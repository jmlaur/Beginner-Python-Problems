import random

#1
magic_number = random.randint(1, 100)
easy_or_hard = input("easy/hard: ")
count = 0

#easy
if easy_or_hard == "easy":
    while count <= 10:
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1
        if guess > magic_number:
            print("Too high!")
            print("Count:", count)
        elif guess < magic_number:
            print("Too low!")
            print("Count:", count)
        elif guess == magic_number:
            print("Correct!")
            break;
#hard
if easy_or_hard == "hard":
    while count <= 5:
        guess = int(input("Guess a number between 1 and 100: "))
        count += 1
        if guess > magic_number:
            print("Too high!")
            print("Count:", count)
        elif guess < magic_number:
            print("Too low!")
            print("Count:", count)
        elif guess == magic_number:
            print("Correct!")
            break;



#2

print("#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...")
num1 = 1
num2 = 1
while True:
    num1 += num2
    print(num1)
    num2 += num1
    if num2 < 4000000:
        print(num2)
    else:
        break;
    
