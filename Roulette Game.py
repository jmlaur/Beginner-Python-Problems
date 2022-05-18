import random



#User bets even/odd.
c = input("Bet even/odd.")
if c == "odd":
    print("Odd")
elif c == "even":
    print("Even")
else:
    print("broken")
#User bets a color.
color = input("Bet a color (red, black): ")


wheel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

#Wheel spins and lands on a random number
spin = random.randint(1, 36)
print("Spin:", spin)

if (spin % 2) > 0:
    a = 1
    x = "Odd"
    print(x)
elif (spin % 2) == 0:
    a = 0
    x = "Even"
    print(x)
else:
    x = "broken"

if spin == 1 or spin == 3 or spin == 5 or spin == 7 or spin == 9 or spin == 12 or spin == 14 or spin == 16 or spin == 18 or spin == 19 or spin == 21 or spin == 23 or spin == 25 or spin == 27 or spin == 30 or spin == 32 or spin == 34 or spin == 36:
    y = "red"
    print("Red")
else:
    y = "black"
    print("Black")

#If number picked is odd + spinned number is odd + spinned number is red and user picked red, they win odd.
if c == "odd" and a > 0 and color.lower() == "red":
        print("Won odd.")
#If number picked is even + spinned number is even + spinned number is red and user picked red, they win even.
elif c == "even" and a == 0 and color.lower() == "red":
        print("Won even.")
#If number picked is even + spinned number is even + spinned number is black and user picked black, they win even.
elif c == "even" and a == 0 and color.lower() == "black":
        print("Won even.")
#If number picked is odd + spinned number is odd + spinned number is black and user picked black, they win odd.
elif c == "odd" and a > 0 and color.lower() == "black":
        print("Won odd.")
#Any other combination results in a loss.
else:
    print("You lost.")

