import random
import sqlite3


def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    return int(input())


def sub_menu():
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
    return int(input())


def generate_pin():
    random.seed()
    # pin in format 1234
    return str(random.randint(1000, 9999))


def luhn_check(value):
    digits = list(map(int, str(value)))
    oddSum = sum(digits[-1::-2])
    evnSum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (oddSum + evnSum) % 10 == 0


def generate_card(prefix):

    random.seed()

    # credit card format
    # 400000 + 123456789

    card = ""

    while True:
        valid = 1
        card = str(prefix) + str(random.randint(1000000000, 9999999999))

        # correct credit card
        if luhn_check(card): break

    return card


def insert_card(number, pin, balance):

    try:
        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO card (number, pin, balance) VALUES (?, ?, ?);"""

        data_tuple = (str(number), str(pin), balance)
        #print(data_tuple)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        #print("Python Variables inserted successfully into SqliteDb_developers table")

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")


def check_card_pin(card, pin):

    sqliteConnection = sqlite3.connect('card.s3db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_with_param = "SELECT number FROM card WHERE number = '{}' and pin = '{}'".format(card, pin)

    cursor.execute(sqlite_insert_with_param)

    results = cursor.fetchone()

    if sqliteConnection:
        sqliteConnection.close()

    # card doesn't exist
    if results is None: return 1

    # card exist
    return 0


def add_card():

    while True:

        # generate card number
        card = generate_card("400000")

        # check if card exist in the database
        stop = check_card(card)
        # if card exists, generate other number
        if stop:
            continue

        # generate pin
        pin = generate_pin()

        # insert credit card into teh database
        insert_card(card, pin, 0)

        print(f"Your card has been created")
        print(f"Your card number:")
        print(f"{card}")
        print(f"Your card PIN:")
        print(f"{pin}")

        break


def check_card(card):

    sqliteConnection = sqlite3.connect('card.s3db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_with_param = "SELECT number FROM card WHERE number = '{}'".format(card)

    cursor.execute(sqlite_insert_with_param)

    results = cursor.fetchone()

    if sqliteConnection:
        sqliteConnection.close()

    # card doesn't exist
    if results is None:
        return 0

    # card exist
    return 1


def get_balance(card, pin):

    sqliteConnection = sqlite3.connect('card.s3db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_with_param = "SELECT balance FROM card WHERE number = '{}' and pin = '{}'".format(card, pin)

    cursor.execute(sqlite_insert_with_param)

    results = cursor.fetchone()

    if sqliteConnection:
        sqliteConnection.close()

    # card don't exist
    if results is None:
        return 0

    # card exist
    return results[0]


def add_income(card, pin):

    try:
        print(f"\nEnter income:")
        income = input()

        sqliteConnection = sqlite3.connect('card.s3db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_with_param = "UPDATE card SET balance = balance + {} WHERE number = '{}' and pin = '{}'".format(income, card, pin)

        cursor.execute(sqlite_insert_with_param)

        sqliteConnection.commit()

        print(f"Income was added!\n")

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")


def do_transfer(card, pin):

    print("Enter card number:")
    transfer_card = input()

    if luhn_check(transfer_card) == 0:
        print("Probably you made a mistake in the card number.Please try again!")
        return
    if check_card(transfer_card) == 0:
        print("Such a card does not exist.")
        return

    print("Enter how much money you want to transfer:")
    balance = input()

    card_balance = get_balance(card, pin)

    if int(balance) > int(card_balance):
        print("Not enough money!")
        return

    sqliteConnection = sqlite3.connect('card.s3db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_with_param = "UPDATE card SET balance = balance + {} WHERE number = '{}'".format(balance, transfer_card)
    cursor.execute(sqlite_insert_with_param)

    sqlite_insert_with_param = "UPDATE card SET balance = balance - {} WHERE number = '{}' and pin = '{}'".format(balance, card, pin)
    cursor.execute(sqlite_insert_with_param)

    sqliteConnection.commit()

    if sqliteConnection:
        sqliteConnection.close()

    print("Success!")

    return


def close_account(card, pin):

    sqliteConnection = sqlite3.connect('card.s3db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_with_param = "DELETE FROM card WHERE number = '{}' and pin = '{}'".format(card, pin)

    cursor.execute(sqlite_insert_with_param)

    print("The account has been closed!")

    sqliteConnection.commit()
    sqliteConnection.close()


if __name__ == "__main__":

    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS card;")
    cursor.execute('''CREATE TABLE IF NOT EXISTS card (id integer not null primary key autoincrement, 
                                                        number text, 
                                                        pin text, 
                                                        balance integer default 0);''')
    conn.commit()
    conn.close()

    while True:

        option = menu()
        print("")

        # 0. Exit
        if option == 0:
            print("Bye!")
            break

        # 1. Create an account
        elif option == 1:
            add_card()

        # 2. Log into account
        elif option == 2:

            card = input("Enter your card number:\n")
            pin  = input("Enter your PIN:\n")

            if check_card_pin(card, pin):
                print("Wrong card number or PIN!")
                continue

            print("You have successfully logged in!")

            stop = 0
            while True:
                sub_option = sub_menu()

                # 0. Exit
                if sub_option == 0:
                    print("Bye!")
                    stop = 1
                    break

                # 1. Balance
                elif sub_option == 1:
                    balance = get_balance(card, pin)
                    print(f"Balance {balance}")

                # 2. Add income
                elif sub_option == 2:
                    add_income(card, pin)

                # 3. Do transfer
                elif sub_option == 3:
                    do_transfer(card, pin)

                # 4. Close account
                elif sub_option == 4:
                    close_account(card, pin)

                # 5. Log out
                elif sub_option == 5:
                    print("You have successfully logged out!")
                    break

            if stop:
                break
