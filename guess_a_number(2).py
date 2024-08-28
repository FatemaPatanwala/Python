import random

print("The computer is guessing a number.")
a=9
attempt=0

for i in range(0,5):
    b=int(input("Enter a number:"))
    attempt+=1
    if attempt==5:
        print("You lose")
    elif b>a:
        print("Your guessed number is high, TRY A LOWER NUMBER!")
    elif b<a:
        print("Your guessed number is low, TRY A GREATER NUMBER!")
    elif b==a:
        print("You guessed it correct.")
        break