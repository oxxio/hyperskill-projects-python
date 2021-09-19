def input_dimension():
    while True:
        dimension = input("Enter your board dimensions: ").split()
        len_x1 = 0
        len_y1 = 0
        if len(dimension) != 2:
            print("Invalid dimensions!")
            continue
        try:
            len_x1 = int(dimension[0])
            len_y1 = int(dimension[1])
        except ValueError:
            print("Invalid dimensions!")
            continue
        if len_x1 <= 0 or len_y1 <= 0:
            print("Invalid dimensions!")
        else:
            break
    return len_x1, len_y1


def input_starting():
    while True:
        position = input("Enter the knight's starting position: ").split()
        x1, y1 = 0, 0
        if len(position) != 2:
            print("Invalid dimensions!")
            continue
        try:
            x1 = int(position[0])
            y1 = int(position[1])
        except ValueError:
            print("Invalid dimensions!")
            continue
        if not 1 <= x1 <= len_x or not 1 <= y1 <= len_y:
            print("Invalid dimensions!")
        else:
            break
    return x1, y1


def create_board():
    for _i in range(len_x):
        current_row = []
        for _j in range(len_y):
            current_row.append("_")
        board.append(current_row)


def print_board(board1):
    max_len = len(str(len_x * len_y))
    print(" " + "-" * (len_x * (max_len + 1) + 3))
    for i in range(len_y, 0, -1):
        s = ""
        for j in range(1, len_x + 1):
            if board1[j - 1][i - 1] != '_':
                s += " " + " " * (max_len - len(board1[j - 1][i - 1])) + board1[j - 1][i - 1]
            elif count(board1, j, i, 'X') != 0:
                next_count = str(count(board1, j, i, '_'))
                s += " " + " " * (max_len - len(next_count)) + next_count
            else:
                s += " " + "_" * max_len
        print(f"{i}|{s} |")
    print(" " + "-" * (len_x * (max_len + 1) + 3))
    s = ''
    for i in range(len_x):
        s += " " * max_len + str(i + 1)
    print("  " + s + " ")
    print()


def count(board1, x1, y1, symbol):
    value = 0
    if x1 + 1 <= len_x and y1 + 2 <= len_y and board1[x1][y1 + 1] == symbol:
        value += 1
    if x1 + 1 <= len_x and y1 - 2 > 0 and board1[x1][y1 - 3] == symbol:
        value += 1
    if x1 - 1 > 0 and y1 + 2 <= len_y and board1[x1 - 2][y1 + 1] == symbol:
        value += 1
    if x1 - 1 > 0 and y1 - 2 > 0 and board1[x1 - 2][y1 - 3] == symbol:
        value += 1
    if x1 + 2 <= len_x and y1 + 1 <= len_y and board1[x1 + 1][y1] == symbol:
        value += 1
    if x1 + 2 <= len_x and y1 - 1 > 0 and board1[x1 + 1][y1 - 2] == symbol:
        value += 1
    if x1 - 2 > 0 and y1 + 1 <= len_y and board1[x1 - 3][y1] == symbol:
        value += 1
    if x1 - 2 > 0 and y1 - 1 > 0 and board1[x1 - 3][y1 - 2] == symbol:
        value += 1
    return value


def move(board1, new_x1, new_y1):
    board2 = []
    for i in range(len_x):
        current_row = []
        for j in range(len_y):
            if board1[i][j] == 'X':
                current_row.append('*')
            else:
                current_row.append(board1[i][j])
        board2.append(current_row)
    board2[new_x1 - 1][new_y1 - 1] = "X"
    return board2


def next_step(board1, new_x1, new_y1, index):
    board2 = []
    for i in range(len_x):
        current_row = []
        for j in range(len_y):
            current_row.append(board1[i][j])
        board2.append(current_row)
    board2[new_x1 - 1][new_y1 - 1] = str(index)
    return board2


def check_solution(board1):
    total = 0
    for i in range(len_x):
        for j in range(len_y):
            if board1[i][j] == '_' and count(board1, i + 1, j + 1, 'X') != 0:
                board2 = move(board1, i + 1, j + 1)
                if check_solution(board2):
                    return True
            elif board1[i][j] in '*X':
                total += 1
    return total == len_x * len_y


def play_game(board1):
    print_board(board1)
    invalid = False
    count_squares = 1
    while True:
        movie = input("Invalid move! Enter your next move: " if invalid else 'Enter your next move: ').split()
        new_x = int(movie[0])
        new_y = int(movie[1])
        if board1[new_x - 1][new_y - 1] != '_' or count(board1, new_x, new_y, 'X') == 0:
            invalid = True
        else:
            invalid = False
            board1 = move(board1, new_x, new_y)
            count_squares += 1
            if count(board1, new_x, new_y, '_') == 0:
                if len_x * len_y == count_squares:
                    print('What a great tour! Congratulations!')
                else:
                    print('No more possible moves!')
                    print(f'Your knight visited {count_squares} squares!')
                break
            print_board(board1)


def print_solution(board1):
    board2 = fill_board(board1, 1)
    print_board(board2)


def fill_board(board1, index):
    for i in range(len_x):
        for j in range(len_y):
            if board1[i][j] == '_' and count(board1, i + 1, j + 1, str(index)) != 0:
                board2 = next_step(board1, i + 1, j + 1, index + 1)
                if index + 1 == len_x * len_y:
                    return board2
                board3 = fill_board(board2, index + 1)
                if board3 is not None:
                    return board3
    return None


board = []
len_x, len_y = input_dimension()
create_board()
x, y = input_starting()
board[x - 1][y - 1] = "X"
while True:
    try_puzzle = input('Do you want to try the puzzle? (y/n): ')
    if try_puzzle == 'y':
        if not check_solution(list(board)):
            print('No solution exists!')
            exit()
        play_game(board)
        break
    elif try_puzzle == 'n':
        if not check_solution(list(board)):
            print('No solution exists!')
            exit()
        board[x - 1][y - 1] = "1"
        print("Here's the solution!")
        print_solution(board)
        break
    else:
        print('Invalid dimensions!')

