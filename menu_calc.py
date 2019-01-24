menu_list = [[1, "Chicken Strips", 3.50], [2, "French Fries", 2.50], [3, "Hamburger", 4.00], [4, "Hot Dog", 3.50],
             [5, "Large Drink", 1.75], [6, "Medium Drink", 1.50], [7, "Milk Shake", 2.25], [8, "Salad", 3.75],
             [9, "Small Drink", 1.25]]

order_total = 0
order_again = True

while order_again:
    order = input("\nPlease enter your order number: ")
    order_list = list(map(int, order))
    for i in order_list:
        print("{} - ${:0,.2f}".format(menu_list[i-1][1], menu_list[i-1][2]))
        order_total = order_total + menu_list[i-1][2]
    print("\nOrder Total: ${:0,.2f}".format(order_total))
    order_total = 0
    order_list = []
    order_again = input("Would you like to place another order (Yes/No)")
    if order_again == "Yes":
        order_again = True
    elif order_again == "No":
        order_again = False
    else:
        print("Invalid Entry")
        order_again = False
