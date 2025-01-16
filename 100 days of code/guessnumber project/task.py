import random

from art import logo

print(logo)

def rule(times):
    while(times>0):
            print(f"You have{times} attempts remaining to guess the number. ")
            guess=int(input("Make a guess:"))
            if guess<number:
                print("Too low.\nGuess again.")
            else:
                print("Too high\nGuess again.")
            times-=1
            if guess==number:
                print(f"You got it! The answer was{number}")
            if times == 0:
                print("You've run out of guesses. Refresh the page to run again.")


number=random.randint(1,100)
print("Welcome to the number guessing game!")
print("I.m thinking of a number between 1 and 100.")
choice=input("Choose a difficulty.Type 'easy' or 'hard':").lower()
if choice=='easy':

    rule(10)
elif choice=='hard':

    rule(5)





