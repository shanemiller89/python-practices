def calc_dollars(pennies, nickels, dimes, quarters):
    piggy_bank = {
        "pennies": pennies,
        "nickels": nickels,
        "dimes": dimes,
        "quarters": quarters
    }
    dollar_amount = (piggy_bank["pennies"] / 100) + (piggy_bank["nickels"] / 20) + (piggy_bank["dimes"] / 10) + (piggy_bank["quarters"] / 4)
    print(f"You have {dollar_amount} in change.")

calc_dollars(741, 32, 756, 973)