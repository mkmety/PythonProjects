menu_list = [[1, "Chicken Strips", 3.50], [2, "French Fries", 2.50], [3, "Hamburger", 4.00], [5, "Large Drink", 1.75]
    , [6, "Medium Drink", 1.50], [7, "Milk Shake", 2.25], [8, "Salad", 3.75], [9, "Small Drink", 1.25]]

#print(menu_list[0][1])

order = input("Please enter your order number: ")

order_list = list(map(int, order))
order_total = 0

for i in order_list:
    if i == 1:
        print(menu_list[0][1])
        order_total = order_total + menu_list[0][2]
    elif i == 2:
        print(menu_list[1][1])
        order_total = order_total + menu_list[1][2]
print("Order Total: ${}".format(order_total))
