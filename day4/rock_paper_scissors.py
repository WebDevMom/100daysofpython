import random
select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

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
print("\nYou chose:")
if select == 0:
    print(rock)
elif select == 1:
    print(paper)
else:
     print(scissors)
print("\nComputer chose:")
computer_select = random.randint(0, 2)
if computer_select == 0:
    print(rock)
elif computer_select == 1:
    print(paper)
else:
     print(scissors)

#decide if player won lost or tied
if computer_select == select:   
    print("You Tied") 



#computer 0 player 1- you win
#computer 0 player 2- you lose

#computer 1 player 2 - you win
#computer 1 player 0 - you lose

#computer 2 player 0 - you win
#computer 2 player 1 - you lose


#Type 0 for Rock, 1 for Paper or 2 for Scissors