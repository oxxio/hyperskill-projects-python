def chk_cells(inp_str, out_str, nr1, nr2, nr3):

    return_string = None

    if inp_str[nr1] == inp_str[nr2] and inp_str[nr2] == inp_str[nr3] and (inp_str[nr1] == "X" or inp_str[nr1] == "O"):
        # if out_str is not None means that we we have two winners
        return_string = ("Impossible" if out_str is not None else f"{inp_str[nr1]} wins")

    if return_string is None and out_str is not None: return out_str

    return return_string


def validations(inp_str):

    out_str = None

    # chek all possible combinations
    out_str = chk_cells(inp_str, out_str, 0, 1, 2)
    out_str = chk_cells(inp_str, out_str, 3, 4, 5)
    out_str = chk_cells(inp_str, out_str, 6, 7, 8)
    out_str = chk_cells(inp_str, out_str, 0, 3, 6)
    out_str = chk_cells(inp_str, out_str, 1, 4, 7)
    out_str = chk_cells(inp_str, out_str, 2, 5, 8)
    out_str = chk_cells(inp_str, out_str, 0, 4, 8)
    out_str = chk_cells(inp_str, out_str, 2, 4, 6)

    # additional validations
    if out_str is None:

        sum_X = sum(True for items in inp_str if items == "X")
        sum_O = sum(True for items in inp_str if items == "O")

        #if sum_X == sum_O and sum_O <= 4:
        #    out_str = "Game not finished"
        if (sum_X == 4 and sum_O == 5) or (sum_X == 5 and sum_O == 4):
            out_str = "Draw"
        elif ((sum_X - 2) >= sum_O) or (((sum_O - 2) >= sum_X)):
            out_str = "Impossible"

    # we have no winner keep going
    if out_str is None:
        return 0
    else:
        # we have a winner
        print(out_str)
        return 1


def print_grid(inp_str):

    # print 3x3 grid
    print("---------")
    for row in range(0, len(inp_str), 3):
        print(f"| {inp_str[row]} {inp_str[row + 1]} {inp_str[row + 2]} |")

    print("---------")

cell = "O"
inp_str = " "*9
list_str = []

#print grid
print_grid(inp_str)

while True:

    if cell == "O": cell = "X"
    else: cell = "O"

    #if i > 2: break
    #if (sum(True for items in inp_str if items == "X" or items == "O")) == 9: break

    x, y = input("Enter the coordinates:").split()

    if not x.isnumeric() or not y.isnumeric():
        print("You should enter numbers!")
        continue
    elif (int(x) < 1 or int(x) > 3) or (int(y) < 1 or int(y) > 3):
        print("Coordinates should be from 1 to 3!")
        continue

    # I = 3 - Y
    # J = X - 1

    # (J * 3) + 2 - I -> inp_str[index]
    index = (( int(x) - 1 ) * 3 ) + 2 - ( 3 - int(y) )

    list_str = list(inp_str)

    if (list_str[int(index)]) == "X" or (list_str[int(index)] == "O"):
        print("This cell is occupied! Choose another one!")
        continue

    list_str[int(index)] = cell
    inp_str = ''.join(list_str)

    print_grid(inp_str)

    # check everything
    if validations(inp_str) == 1:
        break


# I = 3 - Y
# J = X - 1

#  X  Y   J   I   INDEX  J*3       I
# (1, 1)= 0   2    0     0*3 + 2 - 2 = 0
# (1, 2)= 0   1    1     0*3 + 2 - 1 = 1
# (1, 3)= 0   0    2     0*3 + 2 - 0 = 2
# (2, 1)= 1   2    3     1*3 + 2 - 2 = 3
# (2, 2)= 1   1    4     1*3 + 2 - 1 = 4
# (2, 3)= 1   0    5     1*3 + 2 - 0 = 5
# (3, 1)= 2   2    6     2*3 + 2 - 2 = 6
# (3, 2)= 2   1    7     2*3 + 2 - 1 = 7
# (3, 3)= 2   0    8     2*3 + 2 - 0 = 8


# check everything
#validations(inp_str)
#x*2*y
# (1, 1)=2 (1, 2)=4 (1, 3)=6
# (2, 1)= (2, 2)=6 (2, 3)=7
# (3, 1)=7 (3, 2)=8 (3, 3)=9

#0 1 2
#3 4 5
#6 7 8
