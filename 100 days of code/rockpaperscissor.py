import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

sha_choice=[rock,paper,scissors]
random_choice=random.choice(sha_choice)

user_cho=int(input("what do you chose? type 0 for rock, 1 for paper or 2 for scissors"))
if user_cho==0:
    print(rock)
elif user_cho==1:
    print(paper)
elif user_cho==2:
    print(scissors)
else:
    print("invalid choice")
print("computer chose:\n")
if random_choice==rock:
    print(rock)
elif random_choice==paper:
    print(paper)
else:
    print(rock)

if (user_cho==0 and random_choice==paper) or (user_cho==1 and random_choice==scissors) or (user_cho==2 and random_choice==rock):
    print("You lose")
elif(random_choice==rock and user_cho==1) or (random_choice==paper and user_cho==2) or (random_choice==scissors and user_cho==0):
    print("you won")

else:
    print("its a draw invalid")


