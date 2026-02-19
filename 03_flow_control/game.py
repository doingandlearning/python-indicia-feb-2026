import random

# Set up some constants for the game
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

# Set up variables to be used in the game
game_ongoing = True

while game_ongoing:
    # Generate a random number for this game
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)
    
    # Initialize the number of tries the player has made
    count_number_of_tries = 0
    
    # Start the game
    print('Welcome to the number guess game')
    print(f"I'm thinking of a number between {MIN_VALUE} and {MAX_VALUE}")
    
    # Track whether the number has been guessed
    number_not_guessed = True
    
    while number_not_guessed:
        # Get the player's guess
        guess = int(input(GUESS_PROMPT))
        
        # Check for cheat code (-1)
        if guess == -1:
            print(f'The number to guess is {number_to_guess}')
            continue  # Skip the rest of this iteration
        
        # Increment the number of attempts
        count_number_of_tries += 1
        
        # Check if they guessed correctly
        if guess == number_to_guess:
            number_not_guessed = False
        elif guess + 1 == number_to_guess or guess - 1 == number_to_guess:
            print('Sorry wrong number - you were out by 1')
        elif guess < number_to_guess:
            print('Sorry wrong number')
            print('Your guess was lower than the number')
        elif guess > number_to_guess:
            print('Sorry wrong number')
            print('Your guess was higher than the number')
        
        # Check if they've exceeded the maximum number of attempts
        if count_number_of_tries == MAX_NUMBER_OF_GUESSES:
            break
    
    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print(f'You took {count_number_of_tries} goes to complete the game')
    else:
        print("Sorry - you lose")
        print(f'The number you needed to guess was {number_to_guess}')
    
    # Ask if they want to play again
    input_not_accepted = True
    while input_not_accepted:
        play_again = input("Do you want to play again (y/n) or (yes/no)? ")
        play_again = play_again.lower()
        
        if play_again == 'n' or play_again == 'no':
            game_ongoing = False
            input_not_accepted = False
        elif play_again == 'y' or play_again == 'yes':
            input_not_accepted = False
        else:
            print('Invalid input must be y/n or yes/no')

print('Game Over')
