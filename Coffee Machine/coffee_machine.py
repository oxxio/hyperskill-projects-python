water = 400
milk = 540
coffee = 120
cups = 9
money = 550

my_order = """The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money"""


def action_buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

    try:
        buy = int(input())
    except ValueError:
        return

    global water
    global milk
    global coffee
    global money
    global cups

    print(buy)

    if 1 < buy and buy > 3 :
        return
    if buy == 1:
        water -= 250
        if water < 0 :
            print("Sorry, not enough water!")
            water += 250
            return

        coffee -= 16
        if coffee < 0 :
            print("Sorry, not enough coffee!")
            water += 16
            return

        money += 4

    if buy == 2:
        water -= 350
        if water < 0 :
            print("Sorry, not enough water!")
            water += 350
            return

        milk -= 75
        if milk < 0 :
            print("Sorry, not enough milk!")
            water += 75
            return

        coffee -= 20
        if coffee < 0 :
            print("Sorry, not enough coffee!")
            water += 20
            return

        money += 7

    if buy == 3:
        water -= 200
        if water < 0 :
            print("Sorry, not enough water!")
            water += 200
            return

        milk -= 100
        if milk < 0 :
            print("Sorry, not enough milk!")
            water += 100
            return

        coffee -= 12
        if coffee < 0 :
            print("Sorry, not enough coffee!")
            water += 12
            return

        money += 6

    cups -= 1

    print("I have enough resources, making you a coffee!")


def action_fill():

    global water
    global milk
    global coffee
    global cups

    print("Write how many ml of water do you want to add:")
    water += int(input())

    print("Write how many ml of milk do you want to add:")
    milk += int(input())

    print("Write how many grams of coffee beans do you want to add:")
    coffee += int(input())

    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())

def action_take():

    global money
    print("")
    print("I gave you $" + str(money))
    print("")
    money -= money


stop = True

while stop :.
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        action_buy()
    elif action == "fill":
        action_fill()
    elif action == "take":
        action_take()
    elif action == "remaining":
        print("")
        money_final = money
        if money_final > 0 :
            money_final = "$" + str(money_final)
        print(my_order.format(water, milk, coffee, cups, money_final))
        continue
    elif action == "exit":
        stop = False





