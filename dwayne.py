ja godīgi, es interneta izgāšanās dēļ neesmu bijis spējīgs sekot līdzi, un tagad vairs panākt nevarēšu.
cik saprotu te vajag iekodēt akmens šķēres papīrīti.
nu neko...

import random
turns = ["rock","scissors","paper"]

human_turn = input("Enter your weapon of choice: ")
computer_turn = random.choice(turns)

print(f"Human: {human_turn} vs. Computer: {computer_turn}")
if human_turn == computer_turn:
  print("Draw!")
elif human_turn == "rock" and computer_turn == "scissors":
  print("Human wins!")
elif human_turn == "paper" and computer_turn == "rock":
  print("Human wins!")
elif human_turn == "scissors" and computer_turn == "rock":
  print("Human wins!")
else:
  print("Computer wins!")
--------------------------------------------------------------------------------

import random
turns = ["rock","scissors","paper"]

human_turn = input("Enter your turn, or type 'exit': ")
  
computer_turn = random.choice(turns)

print(f"Human: {human_turn} vs. Computer: {computer_turn}")
if human_turn == computer_turn:
  print("Draw!")
elif human_turn == "rock" and computer_turn == "scissors":
  print("Human wins!")
elif human_turn == "paper" and computer_turn == "rock":
  print("Human wins!")
elif human_turn == "scissors" and computer_turn == "rock":
  print("Human wins!")
else:
  print("Computer wins!")

if human_turn == 'exit':
  print("Thank you for playing!")
  
print(f"You have played {len(human_turn)-1} times.")
print(human_turn)
print(computer_turn)
