print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount=bill+ bill*tip/100
split=tip_amount/people
final=round(split,2)
print("Each should pay" + str(final))


