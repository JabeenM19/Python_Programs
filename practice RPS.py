#Rock paper scissor:

import random

user_score = 0 
computer_score = 0
CLEAR = "\033[2J"

options = ['rock','paper','scissor']

while True:
    user_input = input("Choose Rock, Paper, Scissor , or q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print("Invalid input, try again")
        continue
    random_num =  random.randint(0,2)
    computer_input = options[random_num]
     
    print("Computer picked: ",str(computer_input))

    if user_input == 'rock' and computer_input == "rock":
        print("Its a Tie")
    elif user_input == 'paper' and computer_input == 'paper':
        print("Its a Tie")
    elif user_input == 'scissor' and computer_input == 'scissor':
        print("Its a Tie")
    elif user_input == 'rock'and computer_input == 'paper':
        print("You lost")
        computer_score += 1
    elif user_input == 'Paper' and computer_input == 'rock':
        print("You won")
        user_score += 1
    elif user_input =='rock' and computer_input == 'scissor':
        print("You won")
        user_score += 1
    elif user_input == 'scissor' and computer_input == 'rock':
        print("You lost")
        computer_score += 1
    elif user_input == 'paper' and computer_input =='scissor':
        print("You lost")
        computer_score += 1
    elif user_input == 'scissor' and computer_input == 'paper':
        print("You won")
        user_score += 1
    else:
        print("Game finished")
        print("User score: ", str(user_score))
        print("computer score: ", str(computer_score))
        if user_score > computer_score:
            print("You won!")
print(CLEAR)