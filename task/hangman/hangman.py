import random

def play_game():

    chosen = list(random.choice(['java', 'python', 'kotlin', 'javascript']))
    hidden = list('-' * len(chosen))
    all_letters = list()

    count = 0
    while count < 8:
        print()
        print("".join(hidden))
        guess = input('Input a letter: ')

        if len(guess) != 1:
            print("You should input a single letter")
        elif guess.isupper() or not guess.isalpha():
            print("Please enter a lowercase English letter")
        elif guess in all_letters:
            print("You've already guessed this letter")
        elif guess in chosen:
            for i in range(len(chosen)):
                if chosen[i] == guess:
                    hidden[i] = guess
        elif guess not in chosen:
            print("That letter doesn't appear in the word")
            count += 1

        all_letters.append(guess)

        if hidden == chosen:
            print("You survived!")
            break

    if hidden != chosen:
        print('You lost!')



print('H A N G M A N')
game_mode = input('Type "play" to play the game, "exit" to quit:')

while game_mode != "exit":

    if game_mode == "play":
        play_game()

    game_mode = input('Type "play" to play the game, "exit" to quit:')

