#Guess it in 3 times
import random
guess = 0
i =0
number = random. randint(1,10)
while i < 3:
    try:
        print("take a guess:")
        guess = int(input())
        i += 1
    except ValueError:
        print("enter a number;")
    else:
        if guess < number:
            print("guess is lower.")
        elif guess > number:
            print("guess is higher.")
        else:
            break
if guess == number:
    print("you Win.")
else:
    print("you lose")
