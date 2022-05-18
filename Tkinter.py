from tkinter import *
#1
name = "jAmEs"
print(name.upper())
print(name.lower())
print(name.title())

#2
quote = "To be or not to be, that is the question."
author = "Shakespeare"
print(author, " once said, ", quote)

#3
name3 = "\tJames\t"
print(name3)
name4 = "James\nJim"
print(name4)

#4
state = "Michigan"
print(state)
print(len(state))

#5
#Window
root = Tk()
#Label
myLabel = Label(root, text="Hello World")
#Show
myLabel.pack()

root.mainloop()
