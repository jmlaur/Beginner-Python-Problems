#1
height = int(input("How tall are you?"))

if height <= 60:
    print("Cost: 5 dollars.")
else:
    print("Cost: 15 dollars.")


#2 Treasure island

lr = input("Welcome to Treasure Island. Your mission is to find the treasure. You're at a crossroad. Where do you want to go? Type 'left' to go left, or 'right' to go right.")

if lr == "left":
    sw = input("You've come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across or 'wait' to wait for a boat.")
    if sw == "wait":
        door = input("You arrive at the island unharmed. There is a hour with 3 doors. One red, one yellow, one blue. Which color do you choose?")
        if door == "blue":
            print("You were eaten by monsters. Game over.")
        elif door == "red":
            print("You were burned by fire. Game over.")
        elif door =="yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("You were killed by a fish. Game over.")
else:
    print("You fell into a hole. Game over.")
