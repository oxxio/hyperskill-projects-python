import random


#random.seed(3)

def check_opt(option):
    select = ["paper", "scissors", "rock"]

    ret_value = 0
    select_num = 0
    if option == "!exit":
        print("Bye!")
        ret_value = -1
    elif option == "scissors":
        if select[select_num] == "rock":
            print("Sorry, but the computer chose rock")
        elif select[select_num] == "scissors":
            print("There is a draw (scissors)")
            ret_value = 50
        elif select[select_num] == "paper":
            print("Well done. The computer chose paper and failed")
            ret_value = 100
    elif option == "paper":
        if select[select_num] == "rock":
            print("Well done. The computer chose rock and failed")
            ret_value = 100
        elif select[select_num] == "scissors":
            print("Sorry, but the computer chose scissors")
        elif select[select_num] == "paper":
            print("There is a draw (paper)")
            ret_value = 50
    elif option == "rock":
        if select[select_num] == "rock":
            print("There is a draw (rock)")
            ret_value = 50
        elif select[select_num] == "scissors":
            print("Well done. The computer chose scissors and failed")
            ret_value = 100
        elif select[select_num] == "paper":
            print("Sorry, but the computer chose paper")
    else:
        print("Invalid input")

    return ret_value


def is_winner(cpu, human, game_input):

    winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }

    win_val = 0

    if cpu in winning_cases[human]:
        win_val = 1

    return win_val


if __name__ == "__main__":

    file_txt = open("rating.txt")

    # dictionary in format {player:score}
    rating = {}

    player = input("Enter your name: ")

    print(f"Hello, {player}")

    # begin value always 0
    rating[player] = 0

    columns = []
    for line in file_txt:
        columns = line.split()
        if columns[0] == player:
            rating[player] = columns[1]
    file_txt.close()

    game_input = input("").split(",")

    print("Okay, let's start")

    win_options = {}
    if len(game_input) == 1:
        game_input = "rock,scissors,paper".split(",")
        win_options["rock"] = "scissors"
        win_options["paper"] = "rock"
        win_options["scissors"] = "paper"
    else:
        for index in range(len(game_input)):
            if index == 0:
                win_options[game_input[index]] = game_input[len(game_input) - 1]
            else:
                win_options[game_input[index]] = game_input[index - 1]


    while True:

        cpu_input = random.choice(list(win_options.keys()))

        user_input = input("")

        score = 0

        # show rating
        if user_input == "!rating":
            print(f"You rating: {rating[player]}")
            continue
        elif user_input == "!exit":
            print("Bye!")
            break
        elif user_input not in list(win_options.keys()):
            print('Invalid input')
            continue
        elif user_input == cpu_input:
            print(f'There is a draw ({cpu_input})')
            score = 50
        elif is_winner(cpu_input, user_input, game_input) == 1:
            print(f'Well done. Computer chose {cpu_input} and failed')
            score = 100
        else:
            print(f'Sorry, but computer chose {cpu_input}')

        rating.update({player : int(rating[player])+int(score)})

