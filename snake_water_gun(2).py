import random
print("SNAKE , WATER, GUN GAME")

n=int(input("Enter the number of rounds you want to play : "))
player=0
computer=0

for i in range(1,n+1):
    a=input("Enter your choice (snake/water/gun) : ").lower()
    choose=["snake","water","gun"]
    b=random.choice(choose)

    if (a=="snake" and b=="water") or(a=="water" and b=="gun") or (a=="gun" and b=="snake"):
        print("You win this round. Computer chose",b)
        player+=1
    elif a==b:
        print("Tie. Play again.")
    else:
        print("You lose this round. Computer chose",b)
        computer+=1

if player>computer:
    print("YOU WIN THE GAME, AS YOU SCORED",player,"AND COMPUTER SCORED", computer)
elif player<computer:
    print("YOU LOSE THIS GAME, AS COMPUTER SCORED", computer,"AND YOU SCORED", player)
else:
    print("GAME TIE, WITH ",player,"SCORES.")

    

