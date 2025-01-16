from art import logo
import random

print(logo)

# Step 1: Initialize the cards and deal two random cards each to the user and computer
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
b = random.sample(cards, 2)  # User's cards
comp = random.sample(cards, 2)  # Computer's cards

# Step 2: Check for an initial Blackjack win/loss condition
if sum(comp) == 21:
    print("You lose, computer wins!")
elif sum(b) == 21:
    print("You win, computer loses!")
    exit()  # End the game if the user wins immediately
elif sum(b) == 21 and sum(comp) == 21:
    print("Draw!")
    exit()  # End the game in case of a draw

# Step 3: Handle the case where the user's score exceeds 21
while sum(b) > 21:
    if 11 in b:
        b[b.index(11)] = 1  # Replace the ace value from 11 to 1
    else:
        break

# Step 4: Show the initial cards
compo = comp[0]
summ = sum(b)
print(f"Your cards: {b}, current score: {summ}")
print(f"Computer's first card: {compo}")

# Step 5: User's turn to draw another card
choicee = input("Type 'y' to draw another card, type 'n' to pass: ")

while choicee == 'y':
    b.append(random.choice(cards))  # Add a new card to the user's hand
    while sum(b) > 21 and 11 in b:
        b[b.index(11)] = 1  # Adjust ace value if score exceeds 21
    summ = sum(b)
    print(f"Your cards: {b}, current score: {summ}")
    if summ > 21:
        print("You went over. You lose!")
        exit()
    choicee = input("Type 'y' to draw another card, type 'n' to pass: ")

# Step 6: Computer's turn to play
while sum(comp) < 17:
    comp.append(random.choice(cards))  # Add a new card to the computer's hand
    while sum(comp) > 21 and 11 in comp:
        comp[comp.index(11)] = 1  # Adjust ace value if score exceeds 21

# Step 7: Compare scores
comp_score = sum(comp)
print(f"Your final hand: {b}, final score: {summ}")
print(f"Computer's final hand: {comp}, final score: {comp_score}")

if comp_score > 21:
    print("Computer went over. You win!")
elif summ > comp_score:
    print("You win!")
elif summ < comp_score:
    print("You lose!")
else:
    print("It's a draw!")
