import random

print("Enter the number of friends joining (including you):")
friends = int(input())

out = {}
i = 1

if friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    while i <= friends:
        name = input()
        out[name] = 0
        i += 1

    print("Enter the total bill value:")
    bill = int(input(""))

    yes_no = input('\n Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if yes_no == "Yes":

        random_name = random.choice(list(out.keys()))
        print(f'\n{random_name} is the lucky one!\n')

        for key, value in out.items():
            if key == random_name:
                continue
            out[key] = round((bill / (friends-1)), 2)
    else:
        print("No one is going to be lucky")
        for key, value in out.items():
            out[key] = round((bill / friends), 2)


    print(out)

