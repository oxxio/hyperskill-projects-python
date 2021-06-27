import requests

dict_rate = {}

main_currency = input("")

r = requests.get('http://www.floatrates.com/daily/' + main_currency.lower() + '.json')
data = r.json()

for code, output in data.items():
    if code == "usd" or code == "eur":
        dict_rate[code] = output['rate']


while True:
    currency = input("")
    if currency == "":
        break
    amount = int(input(""))

    print("Checking the cache...")

    curr_rate = dict_rate.get(currency.lower())
    if curr_rate == None:
        print("Sorry, but it is not in the cache!")

        r = requests.get('http://www.floatrates.com/daily/' + currency.lower() + '.json')
        data = r.json()

        for code, output in data.items():
            if code == main_currency.lower():

                dict_rate[code] = output['inverseRate']
                dict_rate[currency] = output['inverseRate']

                curr_rate = float(dict_rate[code])
    else:
        print("Oh! It is in the cache!")

    print(f"You received {round(float(curr_rate)*amount, 2)} {currency}.")

