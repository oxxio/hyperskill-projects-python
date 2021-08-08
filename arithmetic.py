import random

def get_number(option):
    num = 0
    while True:
        try:
            num = input()

            if len(num) == 0:
                print("Incorrect format." if option == 1 else "Wrong format! Try again.")
            elif (num.isnumeric() or (num[0] == "-" and num[1:].isnumeric())) and option == 2:
                break
            elif (int(num) == 1 or int(num) == 2) and option == 1:
                break
            else:
                print("Incorrect format." if option == 1 else "Wrong format! Try again.")
        except ValueError:
            print("Incorrect format." if option == 1 else "Wrong format! Try again.")
            continue

    return num

if __name__ == '__main__':

    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11 - 29")

    choice = int(get_number(1))

    i = 0
    passed = 0
    while True:
        i += 1
        if i > 5:
            break

        if choice == 2:
            first = random.randrange(11,30)
            print(f"{first}")
        else:
            first = random.randrange(2,9)
            second = random.randrange(2,9)
            random.seed()
            operation = random.choice('+-*')
            print(f"{first} {operation} {second}")

        num = int(get_number(2))

        if choice == 2:
            if ((int(first) * int(first)) == num):
                passed += 1
                print("Right!")
            else:
                print("Wrong!")

        else:
            if operation == "+":
                if ((int(first) + int(second)) == num):
                    passed += 1
                    print("Right!")
                else:
                    print("Wrong!")
            elif operation == "*":
                if ((int(first) * int(second)) == num):
                    passed += 1
                    print("Right!")
                else:
                    print("Wrong!")
            elif operation == "-":
                if ((int(first) - int(second)) == num):
                    passed += 1
                    print("Right!")
                else:
                    print("Wrong!")

    print(f"Your mark is {passed}/5 Would you like to save the result? Enter yes or no.")

    file_select = input().upper()
    if file_select == "YES" or file_select == "Y":
        name = input("What is your name?\n")

        f = open("results.txt", "a")
        if choice == 1:
            f.write(f'{name}: {passed}/5 in level {choice} (simple operations with numbers 2-9)')
        else:
            f.write(f'{name}: {passed}/5 in level {choice} (integral squares of 11 - 29)')
        f.close()

        print('The results are saved in "results.txt".')
