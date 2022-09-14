# Nickname assignment
import random

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
print("Hello", firstname, lastname)

nicknames = ["Crusher", "the Scientist", "Twinkle-toes", "the Coder", "the Jester", "the Sloth", "Quicksilver"]


#Menu
loop = True
while loop:
    print(" ")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display all Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    print(" ")
    
    slc = int(input("Enter selection 1-6: "))
    print(" ")

    if slc == 1:
        
        firstname = str(input("Enter your first name: "))
        lastname = str(input("Enter your last name: "))
        print(firstname, lastname)
    elif slc == 2:
        
        print(firstname, nicknames[random.randint(0, len(nicknames))], lastname)
    elif slc == 3:

        for i in nicknames:
            print(firstname, i, lastname)
    elif slc == 4:
        nnameToAdd = input("Please enter a new nickname : ")
        if nnameToAdd in nicknames:
            print(nnameToAdd, " already on the list!")
        else:
            nicknames.append(nnameToAdd)
            print("Nickname", nnameToAdd, "added!")
    elif slc == 5:
        nnameToRemove = input("Please enter a nickname to remove: ")
        if nnameToRemove in nicknames:
            nicknames.remove(nnameToRemove)
            print(nnameToRemove, "removed from the list!")
        else: 
            print("Nickname", nnameToRemove, "not found in list!")
    elif slc == 6:
      print("Bye-Bye")
      loop = False 