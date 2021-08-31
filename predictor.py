import random

def get_numbers():
    test_string = ""
    while True:
        print('\nPrint a random string containing 0 or 1:')
        input_str = input()
        if input_str == "enough":
            test_string = input_str
            break
        again = 0
        for i in input_str:
            if i not in ["0", "1"]:
                again = 1
            else:
                test_string += i
        if again == 0:
            break
    return test_string

if __name__ == "__main__":

    triads = {'000': [0, 0], '001': [0, 0],
              '010': [0, 0], '011': [0, 0],
              '100': [0, 0], '101': [0, 0],
              '110': [0, 0], '111': [0, 0]}
    balance = 1000
    out_num = ""
    print('Please give AI some data to learn...')
    print('The current data length is 0, 100 symbols left')
    print('Print a random string containing 0 or 1:')
    print()
    while True:
        in_num = input()
        for num in in_num:
            if not num.isdigit():
                continue
            if num in ["0", "1"]:
                out_num += num
        if len(out_num) < 100:
            print(f'Current data length is {len(out_num)}, {100 - len(out_num)} symbols left')
        else:
            break
    print()
    print('Final data string:')
    print(out_num)
    for i in range(len(out_num) - 3):
        key = str(out_num[i] + out_num[i + 1] + out_num[i + 2])
        if key in ["000", "001", "010", "011", "100", "101", "110", "111"]:
            if int(out_num[i + 3]) == 0:
                triads[key][0] += 1
            else:
                triads[key][1] += 1
    print('\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print('Otherwise, you earn $1. Print \"enough\" to leave the game. Let\'s go!')
    test_string = get_numbers()
    while test_string != "enough":
        if test_string == "enough":
            break
        print("prediction:")
        prediction = list("x" * len(test_string))
        for i in range(3):
            prediction[i] = str(random.choice([0, 1]))
        for i in range(3, len(prediction)):
            reference = test_string[(i - 3):i]
            if triads[reference][0] > triads[reference][-1]:
                prediction[i] = "0"
            elif triads[reference][0] < triads[reference][-1]:
                prediction[i] = "1"
            else:
                prediction[i] = str(random.choice([0, 1]))
        print("".join(prediction))
        print()
        correct = 0
        for i in range(3, len(prediction)):
            if prediction[i] == test_string[i]:
                correct += 1
                balance -= 1
            else:
                balance += 1
        correct_rate = round((correct / (len(prediction) -3)) * 100, 2)
        print(f"Computer guessed right {correct} out of {len(prediction) -3} symbols ({correct_rate} %)")
        print(f"Your balance is now ${balance}")
        test_string = get_numbers()
    print('Game over!')