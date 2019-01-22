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

if standard == grams or Grams:
    total_penny = round(int(penny_weight / penny_weight_grams))
    total_nickel = round(int(nickel_weight / nickel_weight_grams))
    total_dime = round(int(dime_weight / dime_weight_grams))
    total_quarter = round(int(quarter_weight / quarter_weight_grams))
    total_half_dollar = round(int(half_dollar_weight / half_dollar_weight_grams))
    total_golden_dollar = round(int(golden_dollar_weight / golden_dollar_weight_grams))

    amount_penny = str(total_penny * .01)
    amount_nickel = str(total_nickel * .05)
    amount_dime = str(total_dime * .1)
    amount_quarter = str(total_quarter * .25)
    amount_half_dollar = str(total_half_dollar * .5)
    amount_golden_dollar = str(total_golden_dollar * 1)
    
    total_penny_rolls = str(total_penny / penny_roll_count)
    total_nickel_rolls = str(total_nickel / nickel_roll_count)
    total_dime_rolls = str(total_dime / dime_roll_count)
    total_quarter_rolls = str(total_quarter / quarter_roll_count)
    total_half_dollar_rolls = str(total_half_dollar / half_dollar_roll_count)
    total_golden_dollar_rolls = str(total_golden_dollar / golden_dollar_roll_count)
    
    
    









