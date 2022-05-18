import random
amt = 100
wheel = ['CHERRY', 'STAR', 'MONEY_BAG']
current = []

while amt != 0:
    money = int(input("How much money do you want to bet?: "))
    for i in range(3):
        x = random.choice(wheel)
        current.append(x)
    print(*current, sep=' ')
    if current[0] == current[1] and current[0] == current[2] and current[1] == current[2]:
        print("You win!")
        amt += money
        print(amt, "dollars left.")
    if current[0] != current[1] or current[0] != current[2] or current[1] != current[2]:
        print("You lose!")
        amt -= money
        print(amt, "dollars left.")
    current.clear()
