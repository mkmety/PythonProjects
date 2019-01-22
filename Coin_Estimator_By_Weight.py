import math
penny_weight_grams = 2.500
nickel_weight_grams = 5.000
dime_weight_grams = 2.268
quarter_weight_grams = 5.670
half_dollar_weight_grams = 11.340
golden_dollar_weight_grams = 8.1

penny_roll_count = 50
nickel_roll_count = 40
dime_roll_count = 50
quarter_roll_count = 40
half_dollar_roll_count = 20
golden_dollar_roll_count = 50

print("Welcome to the Coin Estimator by Weight tool.\n\nThis tool will allow you to enter in the weight of each "
      "type of coin you possess, tell you how many coin wrappers you will need, how many coins you have, and the "
      "estimated total value of all of your money.\n")

standard = input("Would you like to measure the weight of your coins in grams or ounces? ")

penny_weight = round(float(input("\nHow many " + standard + " of pennies do you have? ")))
nickel_weight = round(float(input("How many " + standard + " of nickels do you have? ")))
dime_weight = round(float(input("How many " + standard + " of dimes do you have? ")))
quarter_weight = round(float(input("How many " + standard + " of quarters do you have? ")))
half_dollar_weight = round(float(input("How many " + standard + " of half dollars do you have? ")))
golden_dollar_weight = round(float(input("How many " + standard + " of golden dollars do you have? ")))

if standard == "grams":
    total_penny = round(float(penny_weight / penny_weight_grams))
    total_nickel = round(float(nickel_weight / nickel_weight_grams))
    total_dime = round(float(dime_weight / dime_weight_grams))
    total_quarter = round(float(quarter_weight / quarter_weight_grams))
    total_half_dollar = round(float(half_dollar_weight / half_dollar_weight_grams))
    total_golden_dollar = round(float(golden_dollar_weight / golden_dollar_weight_grams))

    amount_penny = str(total_penny * .01)
    amount_nickel = str(total_nickel * .05)
    amount_dime = str(total_dime * .1)
    amount_quarter = str(total_quarter * .25)
    amount_half_dollar = str(total_half_dollar * .5)
    amount_golden_dollar = str(total_golden_dollar * 1)

    total_penny_rolls = str(math.ceil((total_penny / penny_roll_count)))
    total_nickel_rolls = str(math.ceil((total_nickel / nickel_roll_count)))
    total_dime_rolls = str(math.ceil((total_dime / dime_roll_count)))
    total_quarter_rolls = str(math.ceil((total_quarter / quarter_roll_count)))
    total_half_dollar_rolls = str(math.ceil((total_half_dollar / half_dollar_roll_count)))
    total_golden_dollar_rolls = str(math.ceil((total_golden_dollar / golden_dollar_roll_count)))

    print("\nYou have {} pennies worth ".format(total_penny) + amount_penny + ".")
    print("You will need " + total_penny_rolls + " penny wrappers")

    print("\nYou have {} nickels worth ".format(total_nickel) + amount_nickel + ".")
    print("You will need " + total_nickel_rolls + " nickel wrappers")

    print("\nYou have {} dimes worth ".format(total_dime) + amount_dime + ".")
    print("You will need " + total_dime_rolls + " dime wrappers")

    print("\nYou have {} quarters worth ".format(total_quarter) + amount_quarter + ".")
    print("You will need " + total_quarter_rolls + " quarter wrappers")

    print("\nYou have {} half dollars worth ".format(total_half_dollar) + amount_half_dollar + ".")
    print("You will need " + total_half_dollar_rolls + " half dollar wrappers")

    print("\nYou have {} golden dollars worth ".format(total_golden_dollar) + amount_golden_dollar + ".")
    print("You will need " + total_golden_dollar_rolls + " golden dollar wrappers")
else:
    print("Haven't gotten to ounces yet")










