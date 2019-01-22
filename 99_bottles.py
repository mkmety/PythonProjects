num_list = list(range(99, 0, -1))

for i in num_list:
    if i == 2:
        print("{0} bottles of beer on the wall. {0} bottles of beer.".format(i))
        print("Take one down and pass it around. {0} bottle of beer on the wall!".format(i-1))
        print("\n")
    elif i == 1:
        print("{0} bottle of beer on the wall. {0} bottle of beer.".format(i))
        print("Take one down and pass it around. No more bottles of beer on the wall!")
    else:
        print("{0} bottles of beer on the wall. {0} bottles of beer.".format(i))
        print("Take one down and pass it around. {0} bottles of beer on the wall!".format(i-1))
        print("\n")
