import random

def guess_the_game():
    game_list = ['Uncharted', 'The Last of US', 'Gta', 'Tomb Raider', 'Valorant','Counter Strike', 'Phasmophobia']
    game_to_guess1 = random.choice(game_list)
    game_to_guess2 = ((game_to_guess1).lower()).replace(' ','')
    hidden_game = ['_'] * len(game_to_guess2)
    attempts = 6

    print("Welcome to my Game name Guessing Game!")
    print(" ".join(hidden_game))

    while attempts > 0 and '_' in hidden_game:
        guess = input(f"Enter a letter (attempts left: {attempts}): ").lower()

        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in game_to_guess2:
            print("Good guess!")
            for i, letter in enumerate(game_to_guess2):
                if letter == guess:
                    hidden_game[i] = guess
        else:
            print("Oops! That letter is not in the game name.")
            attempts -=1
        
        print(" ".join(hidden_game))

    if '_' not in hidden_game:
        print(f"Congratulations gamer! You guessed the game right!!! name: {game_to_guess1}")
    else:
        print(f"Game over mate! The name of the game was: {game_to_guess1}")

guess_the_game()