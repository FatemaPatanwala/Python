import random

print("The computer is guessing a number.")
a=random.randint(1,10)

for i in range(0,5):
    b=int(input("Enter a number:"))
    if b==a:
        print("You guessed it correct. ")
        break
    elif i==5:
        print("You loose")
    elif b>a:
        print("Your guessed number is high, TRY A LOWER NUMBER!")
    elif b<a:
        print("Your guessed number is low, TRY A GREATER NUMBER!")
        
