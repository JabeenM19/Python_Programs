import random

def roll():
    min_value =1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid,try again")
print(players)

max_score = 50
player_score = [0 for i in range(players)]
print(player_score)



while max(player_score) < max_score:
    for  player_index  in range(players):
        print("\n PLayer",player_index+1, "turn has just started \n")
        print("Your Total score is: ",player_score[player_index],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (yes), type q to quit?").lower()
            if should_roll != 'yes':
                break
            value = roll()

            if value == 1:
                print("you rolled a 1, Turn Done!")
                break
            else:
                current_score += value
                print("You rolled a " ,value)
            print("Your current score is: ", current_score)
        player_score[player_index] += current_score
        print("Your Total score is: ",player_score[player_index])
max_score = max(player_score)
player_winning_index = player_score.index(max_score)
print("player number", player_winning_index+1, " is the winner with a score ",max_score )