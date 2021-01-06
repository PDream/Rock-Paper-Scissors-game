import random
random_choice = random.randint(0,2)
#print (random_choice)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

#user_choice = input ("Choose rock or paper or scissors: ")
#print ( user_choice, "and", computer_choice)
user_choice = ""
while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input ("Choose rock or paper or scissors: ")
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and  user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'
#print ("The", winner, "wins!")
if winner == 'Tie':
    print ("No winner! You both chose", computer_choice,", play again!")
else:
    print (winner, "won! The computer chose", computer_choice)
