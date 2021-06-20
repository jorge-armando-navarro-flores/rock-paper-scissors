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

import random
hands = [rock, paper, scissors]

choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if choice < 0 or choice > 2:
  print("Invalid number, you lose")
else:
  playerhand =  hands[choice]
  print(playerhand)
  computerhand = hands[random.randint(0,2)]
  print("computer chose:")
  print(computerhand)

  if computerhand == hands[choice - 1]:
    print("You win")
  elif playerhand != computerhand:
    print("You lose")
  else:
    print("Tie")