print("\nWELCOME TO THE ADVENTURE GAME !")
print("You find yourself standing in front of two caves.")
print("One cave is dark and spooky, and the other is bright and inviting.")
print("Which cave will you enter? (Dark or bright) \n")

choose = int(input("Choose from options(1 or 2) \n 1. Dark and spooky cave \n 2. Bright and inviting cave   : "))

if choose ==1:
    print("\nYou approached the cave and its dark and spooky here .")
    print("You encountered a giant spider!")
    print("What will you do ? Run away or Fight")

    action = int(input("Choose from the given options (1/2) \n 1.Fight \n 2.Run away   :  "))
    if action==1:
        print("You defeated the spider! Well done!")
    elif action==2:
        print("You feared from the spider and ran away. ")
    else:
        print("Invalid input.")

elif choose==2:
    print("\nYou approached the cave and its bright and inviting here .")
    print("You found a chest full of treasure!")
    print("What will you do ?")
          
    action_1 = int(input("1. Take all the treasure\n2. Take a small amount\n3. Leave the treasure   :"))
    if action_1==1:
        print("You take all the treasure and become wealthy!")
    elif action_1==2:
        print("You take a small amount of treasure and leave the rest.")
    elif action_1==3:
        print("You decide to leave the treasure untouched.")
        print("On your way out, you stumble upon a hidden passage leading to an ancient artifact!")
    else:
        print("Invalid choice")

else:
    print("Invalid choice")