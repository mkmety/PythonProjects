while True:
     total_cost = round(float(input("\nEnter total cost: $")), 2)
     amount_given = round(float(input("Enter the amount you were given: $")), 2)
     whole_change_due = round((amount_given - total_cost), 2)

     if whole_change_due > 0:
          bill_change = int(whole_change_due)
          print("You owe the customer ${} in bills.".format(bill_change))
          change_change = round((whole_change_due - bill_change), 2)
          total_quarters = int(change_change / .25)
          total_dimes = int((change_change - (total_quarters * .25)) / .10)
          total_nickels = int((change_change - ((total_quarters * .25) + (total_dimes * .10))) / .05)
          total_pennies = int((change_change - ((total_quarters * .25) + (total_dimes * .10) + (total_nickels * .05))) / .01)
          print("You owe the customer {} quarters.".format(total_quarters))
          print("You owe the customer {} dimes.".format(total_dimes))
          print("You owe the customer {} nickels.".format(total_nickels))
          print("You owe the customer {} pennies.".format(total_pennies))
     else:
          print("The customer did not give you enough money.")
