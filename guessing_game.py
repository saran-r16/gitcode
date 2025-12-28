#Number guessing game
import random
print("Number Guessing Game 1 to 50")
attempt=0
low=0
high=50
guess=random.randint(low,high)
while True:
    n=input("Guess the number :")
    if n.isdigit():
        n=int(n)
        if 0>n or high<n:
            print("Invaild input")
            continue
        elif guess<n:
            attempt+=1
            print("Enter a small number")
        elif guess>n:
            attempt+=1
            print("Enter a bigger number")
        else:
            print("**Got it**")
            break
    else:
        print("---Please Enter Numeric Value---")
print("Guessing attempt is: ",attempt)