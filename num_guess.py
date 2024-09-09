import random
import time
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print("You have 5 chances to guess the correct number.")
print("\n")


def diff_level():
    print("Please select the difficulty level:")
    print("\n")
    choice_dict = {
    "1": "Easy (10 chances)",
    "2": "Medium (5 chances)",
    "3": "Hard (3 chances)"
    }
    for key, value in choice_dict.items():
        print(f"{key}: {value}")
    print("\n")
    type1 = input("Enter your choice: ")
    print("\n")
    
    if type1 == "1":
        print("You have selected the Easy difficulty level,10 chances to guess")
        return 10 # Correct approach for returning max attempts for easy level
    elif type1=='2':
        print("Good, You have selected the Medium difficulty level, 5 chances to guess")
        return 5 # Correct approach for returning max attempts for medium level
    elif type1 =='3':
        print("Great! You have selected the Hard difficulty level, 3 chances to guess")
        return 3 # Correct approach for returning max attempts for hard level
    else:
        print("Invalid choice, Defaulting to Medium difficulty.") # debug step
        return 5 # Correct fallback return if invalid choice



def guess_entry(max_attempts):
    guess = random.randrange(1,101)
    attempts = 0

    start_time = time.time() #start time before the loop
    while attempts < max_attempts:
        try:
            type2 = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue 
        if type2 < guess:
            print("Incorrect! The Number is greater than ",type2)
            hint1 = random.randrange(type2,guess) # for randrange: first argument must be smaller than the second
            print("Hint: The number lies around",hint1)
        elif type2 > guess:
            print("Incorrect! The Number is less than ",type2)
            hint2 = random.randrange(guess,type2)
            print("Hint: The number lies around",hint2)
        else:
            print("Congratulations! You guessed the correct number in",attempts+1,"attempts.")
            break

        attempts +=1
    end_time = time.time() # end time after the loop
    total_time =round((end_time-start_time),2)

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {guess}.")
    print("Time taken: ",total_time,"seconds")


def continue_playing(max_attempts):
    # play multiple rounds: i.e user can continue playing if they want
    gameCount = 0
    type3 = input("Do you wanna continue guessing? (Y/N): ").upper()
    if type3 == 'Y':
        gameCount+=1
        main()
    elif type3 == 'N':
        print("Thank you for playing")
    else:
        quit


def highScore():
    pass
    

def main():
    # Choose difficulty level for each new game
    max_attempts =diff_level() #returns the number of attempts based on the difficulty level chosen.
    
    # Start the guessing game
    guess_entry(max_attempts)

    # Ask if user wants to continue
    continue_playing(max_attempts)

if __name__=='__main__':
    main()

