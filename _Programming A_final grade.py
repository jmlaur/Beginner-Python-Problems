grade = int(input("What is your grade?: "))

if grade >= 94:
    print("You have an A")
elif grade >= 90 and grade < 94:
    print("You have an A-")
elif grade >= 87 and grade < 90:
    print("You have a B+")
elif grade >= 83 and grade < 87:
    print("You have a B")
elif grade >= 80 and grade < 84:
    print("You have a B-")
elif grade >= 77 and grade < 80:
    print("You have a C+")
elif grade >= 73 and grade < 77:
    print("You have a C")
elif grade >= 70 and grade < 73:
    print("You have a C-")
elif grade >= 67 and grade < 70:
    print("You have a D+")
elif grade >= 60 and grade < 67:
    print("You have a D")
elif grade >= 0 and grade < 60:
    print("You have an F")
else:
    print("Incorrect grade value.")
