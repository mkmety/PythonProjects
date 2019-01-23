import math
penny_weight_grams = 2.500
nickel_weight_grams = 5.000
dime_weight_grams = 2.268
quarter_weight_grams = 5.670
half_dollar_weight_grams = 11.340
golden_dollar_weight_grams = 8.1

penny_weight_ounces = 0.0881849
nickel_weight_ounces = 0.17637
dime_weight_ounces = 0.080001346
quarter_weight_ounces = 0.2000034
half_dollar_weight_ounces = 0.40000673
golden_dollar_weight_ounces = 0.285719

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

if standard == "grams":
    penny_weight = round(float(input("\nHow many " + standard + " of pennies do you have? ")))
    nickel_weight = round(float(input("How many " + standard + " of nickels do you have? ")))
    dime_weight = round(float(input("How many " + standard + " of dimes do you have? ")))
    quarter_weight = round(float(input("How many " + standard + " of quarters do you have? ")))
    half_dollar_weight = round(float(input("How many " + standard + " of half dollars do you have? ")))
    golden_dollar_weight = round(float(input("How many " + standard + " of golden dollars do you have? ")))

    total_penny_grams = round(float(penny_weight / penny_weight_grams))
    total_nickel_grams = round(float(nickel_weight / nickel_weight_grams))
    total_dime_grams = round(float(dime_weight / dime_weight_grams))
    total_quarter_grams = round(float(quarter_weight / quarter_weight_grams))
    total_half_dollar_grams = round(float(half_dollar_weight / half_dollar_weight_grams))
    total_golden_dollar_grams = round(float(golden_dollar_weight / golden_dollar_weight_grams))

    amount_penny = round((total_penny_grams * .01), 2)
    amount_nickel = round((total_nickel_grams * .05), 2)
    amount_dime = round((total_dime_grams * .1), 2)
    amount_quarter = round((total_quarter_grams * .25), 2)
    amount_half_dollar = round((total_half_dollar_grams * .5), 2)
    amount_golden_dollar = round((total_golden_dollar_grams * 1), 2)
    overall_amount = round((amount_penny + amount_nickel + amount_dime + amount_quarter + amount_half_dollar \
                     + amount_golden_dollar), 2)

    total_penny_rolls = str(math.ceil((total_penny_grams / penny_roll_count)))
    total_nickel_rolls = str(math.ceil((total_nickel_grams / nickel_roll_count)))
    total_dime_rolls = str(math.ceil((total_dime_grams / dime_roll_count)))
    total_quarter_rolls = str(math.ceil((total_quarter_grams / quarter_roll_count)))
    total_half_dollar_rolls = str(math.ceil((total_half_dollar_grams / half_dollar_roll_count)))
    total_golden_dollar_rolls = str(math.ceil((total_golden_dollar_grams / golden_dollar_roll_count)))

    print("\nYou have {} pennies worth ".format(total_penny_grams) + "${}.".format(amount_penny))
    print("You will need " + total_penny_rolls + " penny wrappers.")

    print("\nYou have {} nickels worth ".format(total_nickel_grams) + "${}".format(amount_nickel))
    print("You will need " + total_nickel_rolls + " nickel wrappers.")

    print("\nYou have {} dimes worth ".format(total_dime_grams) + "${}.".format(amount_dime))
    print("You will need " + total_dime_rolls + " dime wrappers.")

    print("\nYou have {} quarters worth ".format(total_quarter_grams) + "${}.".format(amount_quarter))
    print("You will need " + total_quarter_rolls + " quarter wrappers.")

    print("\nYou have {} half dollars worth ".format(total_half_dollar_grams) + "${}.".format(amount_half_dollar))
    print("You will need " + total_half_dollar_rolls + " half dollar wrappers.")

    print("\nYou have {} golden dollars worth ".format(total_golden_dollar_grams) + "${}.".format(amount_golden_dollar))
    print("You will need " + total_golden_dollar_rolls + " golden dollar wrappers.")

    print("\nYou have a total of ${}".format(overall_amount))
elif standard == "ounces":
    penny_weight = round(float(input("\nHow many " + standard + " of pennies do you have? ")))
    nickel_weight = round(float(input("How many " + standard + " of nickels do you have? ")))
    dime_weight = round(float(input("How many " + standard + " of dimes do you have? ")))
    quarter_weight = round(float(input("How many " + standard + " of quarters do you have? ")))
    half_dollar_weight = round(float(input("How many " + standard + " of half dollars do you have? ")))
    golden_dollar_weight = round(float(input("How many " + standard + " of golden dollars do you have? ")))

    total_penny_ounces = round(float(penny_weight / penny_weight_ounces))
    total_nickel_ounces = round(float(nickel_weight / nickel_weight_ounces))
    total_dime_ounces = round(float(dime_weight / dime_weight_ounces))
    total_quarter_ounces = round(float(quarter_weight / quarter_weight_ounces))
    total_half_dollar_ounces = round(float(half_dollar_weight / half_dollar_weight_ounces))
    total_golden_dollar_ounces = round(float(golden_dollar_weight / golden_dollar_weight_ounces))

    amount_penny_ounces = round((total_penny_ounces * .01), 2)
    amount_nickel_ounces = round((total_nickel_ounces * .05), 2)
    amount_dime_ounces = round((total_dime_ounces * .1), 2)
    amount_quarter_ounces = round((total_quarter_ounces * .25), 2)
    amount_half_dollar_ounces = round((total_half_dollar_ounces * .5), 2)
    amount_golden_dollar_ounces = round((total_golden_dollar_ounces * 1), 2)
    overall_amount_ounces = round((amount_penny_ounces + amount_nickel_ounces + amount_dime_ounces + 
                                   amount_quarter_ounces + amount_half_dollar_ounces + amount_golden_dollar_ounces), 2)

    total_penny_rolls = str(math.ceil((total_penny_ounces / penny_roll_count)))
    total_nickel_rolls = str(math.ceil((total_nickel_ounces / nickel_roll_count)))
    total_dime_rolls = str(math.ceil((total_dime_ounces / dime_roll_count)))
    total_quarter_rolls = str(math.ceil((total_quarter_ounces / quarter_roll_count)))
    total_half_dollar_rolls = str(math.ceil((total_half_dollar_ounces / half_dollar_roll_count)))
    total_golden_dollar_rolls = str(math.ceil((total_golden_dollar_ounces / golden_dollar_roll_count)))

    print("\nYou have {} pennies worth ".format(total_penny_ounces) + "${}.".format(amount_penny_ounces))
    print("You will need " + total_penny_rolls + " penny wrappers.")

    print("\nYou have {} nickels worth ".format(total_nickel_ounces) + "${}".format(amount_nickel_ounces))
    print("You will need " + total_nickel_rolls + " nickel wrappers.")

    print("\nYou have {} dimes worth ".format(total_dime_ounces) + "${}.".format(amount_dime_ounces))
    print("You will need " + total_dime_rolls + " dime wrappers.")

    print("\nYou have {} quarters worth ".format(total_quarter_ounces) + "${}.".format(amount_quarter_ounces))
    print("You will need " + total_quarter_rolls + " quarter wrappers.")

    print("\nYou have {} half dollars worth ".format(total_half_dollar_ounces) +
          "${}.".format(amount_half_dollar_ounces))
    print("You will need " + total_half_dollar_rolls + " half dollar wrappers.")

    print("\nYou have {} golden dollars worth ".format(total_golden_dollar_ounces) +
          "${}.".format(amount_golden_dollar_ounces))
    print("You will need " + total_golden_dollar_rolls + " golden dollar wrappers.")

    print("\nYou have a total of ${}".format(overall_amount_ounces))
else:
    print("This is not a supported weight standard")










