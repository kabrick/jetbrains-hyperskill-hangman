import random

# Write your code here
print("H A N G M A N")
print()

word_list = ['python', 'java', 'kotlin', 'javascript']

while True:
    user_request = input('Type "play" to play the game, "exit" to quit')
    
    if user_request == "play":
        chosen_word = random.choice(word_list)
        chosen_word_list = list(chosen_word)
        user_inputs = []
        guess_tracker = ("- " * len(chosen_word)).split()
        tries = 8
        game_over = False
        play_won = False
        
        while tries > 0 and not game_over:
            print()
            print("".join(guess_tracker))
            
            player_guess = input("Input a letter: ")
            
            if len(player_guess) > 1:
                print("You should input a single letter")
            elif player_guess in user_inputs:
                print("You already typed this letter")
            elif not player_guess.islower():
                print("It is not an ASCII lowercase letter")
            elif player_guess not in chosen_word:
                tries -= 1
                print("No such letter in the word")
            else:
                while player_guess in chosen_word_list:
                    letter_index = chosen_word_list.index(player_guess)
                    chosen_word_list[letter_index] = "*"
                    guess_tracker[letter_index] = player_guess
                    
            user_inputs.append(player_guess)
                
            if "".join(guess_tracker) == chosen_word:
                game_over = True
                play_won = True
            elif tries == 0:
                game_over = True
                
        if play_won:
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")
    elif user_request == "exit":
        break
