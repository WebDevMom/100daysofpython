import random
select = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

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
if select == "0":
    print(rock)
elif select == "1":
    print(paper)
else:
     print(scissors)

#no ideas
computer_select = random.randint(0, 2)
