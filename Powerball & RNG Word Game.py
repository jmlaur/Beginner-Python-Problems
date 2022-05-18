import random

#1 Powerball

num1 = int(input("Number (from 1 to 69): "))
num2 = int(input("Number (from 1 to 69): "))
num3 = int(input("Number (from 1 to 69): "))
num4 = int(input("Number (from 1 to 69): "))
num5 = int(input("Number (from 1 to 69): "))
print(str(num1) + str(num2) + str(num3) + str(num4) + str(num5))
win1 = random.randint(1,69)
win2 = random.randint(1,69)
win3 = random.randint(1,69)
win4 = random.randint(1,69)
win5 = random.randint(1,69)
print(str(win1) + str(win2) + str(win3) + str(win4) + str(win5))


#2 Word Game

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = []
for i in range(5):
    game = random.choice(alphabet)
    list1.append(game)
print(list1)

guess = input("Guess: ")
if len(guess) == 5:
    print("5 Points")
elif len(guess) == 4:
    print("4 Points")
elif len(guess) == 3:
    print("3 Points")
elif len(guess) == 2:
    print("2 Points")
elif len(guess) == 1:
    print("1 Point")
else:
    print("No points")
