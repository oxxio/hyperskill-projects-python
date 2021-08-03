import random

def validate(current, domino, all, final, insert):
    dominoA = current[0]
    dominoB = current[1]
    #         0       -1
    # list[[A, B]...[C, D]]
    first = domino[0]
    last  = domino[-1]
    # left -> [A, B]
    if first[0] == dominoA and insert == 1:
        # [dominoB, dominoA][A, B]
        final.append(dominoB)
        final.append(dominoA)
        if [dominoB, dominoA] in all:
            all.remove([dominoB, dominoA])
        if [dominoA, dominoB] in all:
            all.remove([dominoA, dominoB])
        return 1
    if first[0] == dominoB and insert == 1:
        # [dominoA, dominoB][A, B]
        final.append(dominoA)
        final.append(dominoB)
        if [dominoB, dominoA] in all:
            all.remove([dominoB, dominoA])
        if [dominoA, dominoB] in all:
            all.remove([dominoA, dominoB])
        return 1
    # right -> [C, D]
    if last[1] == dominoA and insert == 0:
        # [C, D][dominoA, dominoB]
        final.append(dominoA)
        final.append(dominoB)
        if [dominoB, dominoA] in all:
            all.remove([dominoB, dominoA])
        if [dominoA, dominoB] in all:
            all.remove([dominoA, dominoB])
        return 1
    if last[1] == dominoB and insert == 0:
        # [C, D][dominoB, dominoA]
        final.append(dominoB)
        final.append(dominoA)
        if [dominoB, dominoA] in all:
            all.remove([dominoB, dominoA])
        if [dominoA, dominoB] in all:
            all.remove([dominoA, dominoB])
        return 1
    return -1

def genDomino(list, all, insert, final):
    while True:
        ranNum = random.randint(0, len(all))
        dominoA = all[ranNum][0]
        dominoB = all[ranNum][1]
        if len(list) == 0:
            final.append([dominoB, dominoA])
            if [dominoB, dominoA] in all:
                all.remove([dominoB, dominoA])
            if [dominoA, dominoB] in all:
                all.remove([dominoA, dominoB])
            break
        else:
            if validate(all(ranNum), list, all, final, insert) == 1:
                break
    return

def printDomino(domino):
    if len(domino) > 6:
        field = f"{domino[0]}{domino[1]}{domino[2]}...{domino[-3]}{domino[-2]}{domino[-1]}"
    else:
        field = "".join(str(x) for x in domino)
    print(field)

def checkGameState():
    state = None
    print(*domino)
    if domino[0][0] == domino[-1][-1] and (sum(x.count(domino[0][0]) for x in domino) == 8):
        state = "It's a draw"
    elif len(stock) == 0 and (len(player) > len(computer)):
        state = "The computer won"
    elif len(player) == 0:
        state = "You won"
    elif len(computer) == 0:
        state = "The computer won"
    return state

if __name__ == "__main__":
    status   = ""
    insert   = 0
    stock    = []
    computer = []
    player   = []
    domino   = []
    # generate 28 out of 48 combinations
    all      = [[a, b] for b in range(7) for a in range(7) if a <= b]
    random.shuffle(all)
    stock    = all[0:14]    # 14 dominos
    computer = all[14:21]   # 7 dominos
    player   = all[21:28]   # 7 dominos
    max_double = max(max(computer), max(player))
    if max_double in computer:
        computer.remove(max_double)
        status = "player"
    else:
        player.remove(max_double)
        status = "computer"
    domino.append(max_double)
    while True:
        print("="*70)
        print(f'Stock size: {len(stock)}')
        print(f'Computer pieces: {len(computer)}')
        print()
        printDomino(domino)
        print()
        print(f'Your pieces:')
        for number, value in enumerate(player):
            print(f'{number+1}:{value}')
        retVal = checkGameState()
        if retVal is not None:
            print(f"Status: The game is over. {retVal}!")
            break
        print()
        listValue = []
        addValue  = []
        retValue  = 0
        if status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
            while True:
                try:
                    error = 0
                    i = int(input())
                    if (i > 0 and i > len(player) + 1) or (i < 0 and (-i > len(player) + 1)):
                        print("Invalid input. Please try again.")
                        error = 1
                    elif i > 0:
                        listValue = player[i - 1]
                        retValue = validate(listValue, domino, all, addValue, 0)
                        if retValue == -1:
                            print("Illegal move. Please try again.")
                            error = 1
                        else:
                            domino.append(addValue)
                            player.remove(listValue)
                    elif i < 0:
                        listValue = player[-i - 1]
                        retValue = validate(listValue, domino, all, addValue, 1)
                        if retValue == -1:
                            print("Illegal move. Please try again.")
                            error = 1
                        else:
                            domino.insert(0, addValue)
                            player.remove(listValue)
                    elif i == 0:
                        randomNum = random.randint(0, len(stock) - 1)
                        player.append(stock[randomNum])
                        stock.remove(stock[randomNum])

                    if error == 1:
                        continue
                    status = "computer"
                except:
                    print("Invalid input. Please try again.")
                    error = 1

                if error == 0:
                    break
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            dum = input()
            while True:
                try:
                    error = 0
                    i = int(random.randint(-len(computer), len(computer)))
                    if i == 0:
                        randomNum = random.randint(0, len(stock) - 1)
                        computer.append(stock[randomNum])
                        stock.remove(stock[randomNum])
                    elif i > 0:
                        listValue = computer[i - 1]
                        retValue = validate(listValue, domino, all, addValue, 0)
                        if retValue == -1:
                            error = 1
                        else:
                            domino.append(addValue)
                            computer.remove(listValue)
                    elif i < 0:
                        listValue = computer[-i - 1]
                        retValue = validate(listValue, domino, all, addValue, 1)
                        if retValue == -1:
                            error = 1
                        else:
                            domino.insert(0, addValue)
                            computer.remove(listValue)

                    if error == 1:
                        continue
                    status = "player"
                except:
                    continue

                if error == 0:
                    break
