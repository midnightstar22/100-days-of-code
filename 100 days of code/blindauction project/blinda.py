from art import logo

print(logo)

# Dictionary to store bids
pgm_dictionary = {}

# Function to collect user input
def inpu():
    name = input("What's your name? ")
    bid = int(input("What is your bid? $"))  # Ensure bid is saved as an integer
    pgm_dictionary[name] = bid
    ans = input("Is there anyone else to bid? Type 'Y' or 'N': ").upper()
    return ans

# Function to find the highest bid
def biddy():
    largest_bid = 0
    winner = ""
    for bidder in pgm_dictionary:
        if pgm_dictionary[bidder] > largest_bid:
            largest_bid = pgm_dictionary[bidder]
            winner = bidder
    print(f"The highest bid is ${largest_bid} by {winner}.")

# Main Program
while True:
    ans = inpu()
    if ans == 'N':
        break
    print("\n" * 100)  # Clears the screen for privacy

biddy()
