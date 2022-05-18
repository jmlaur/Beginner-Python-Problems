import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = []
for i in range(5):
    game = random.choice(alphabet)
    list1.append(game)
print(list1)


guess = input("Guess: ")
word = list(guess)
pts = 0
for i in range(len(word)):
    if word[i] in list1:
        pts += 1
    else:
        pts = 0
print("Points: ", pts)
