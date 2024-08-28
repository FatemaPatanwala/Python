 import random
print("SNAKE , WATER, GUN GAME")
a=input("Enter your choice (snake/water/gun) : ").lower()
choose=["snake","water","gun"]
b=random.choice(choose)


if (a=="snake" and b=="water") or(a=="water" and b=="gun") or (a=="gun" and b=="snake"):
    print("You win. Computer chose",b)
elif a!="snake" or a!="water" or a!="gun":
    print("Invalid input ,TRY AGAIN.")
elif a==b:
    print("Tie. Play again.")
else:
    print("You lose, TRY AGAIN. Computer chose",b)    

