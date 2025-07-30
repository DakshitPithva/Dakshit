# Making Game Guess The Correct Number

import random
n = random.randint(1,100)
a = -1
guess = 0

while(a != n):
    guess +=1
    a = int(input("Guess The Number :"))
    if(a>n):
        print("Guess Lower Number Please")
    else:
        print("Guess Higher Number Please")

if(guess < 5):
    print(f"Congratulation You Guess The Number in {guess} Attempt")
elif(guess > 5 and guess < 20):
    print(f"You Can Guess The Number {guess} Attempt")
else:
    print(f"You Can Guess The Number {guess} Attempt \n You got time to Guess The Number")