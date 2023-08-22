rates={ "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.7974}

# curency exchange rate application

#
# amount = int(input("enter the amount >"))
# from_cur_code = input("enter the source currency code")
# to_cur_code = input("enter the destination currency code")
#
# from_rates=rates.get(from_cur_code)
# to_rates=rates.get(to_cur_code)
# result = (amount/from_rates)*to_rates
# print(result)

from json import load

with open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\currencyexchange\\dbs.json")as f:
    data=load(f)
    rates=data.get("conversion_rates")
    amount = int(input("enter the amount >"))
    from_cur_code = input("enter the source currency code")
    to_cur_code = input("enter the destination currency code")

    from_rates = rates.get(from_cur_code)
    to_rates = rates.get(to_cur_code)
    result = (amount / from_rates) * to_rates
    print(result)

