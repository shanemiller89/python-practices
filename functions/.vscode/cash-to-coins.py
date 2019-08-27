def calc_coins(dollars):
    piggy_bank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    dollar_amount = dollars
    piggy_bank["quarters"] = int(dollar_amount * 4)
    dollar_amount = dollar_amount%4
    piggy_bank["dimes"] = int(dollar_amount * 10)
    dollar_amount = dollar_amount%.10
    piggy_bank["nickels"] = int(dollar_amount * 20)
    dollar_amount = dollar_amount%.05
    piggy_bank["pennies"] = int(dollar_amount * 100)


    print(piggy_bank)

calc_coins(8.69)