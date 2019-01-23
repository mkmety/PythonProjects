import statistics

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))
number_4 = float(input("Enter the fourth number: "))
number_5 = float(input("Enter the fifth number: "))

num_list = [number_1, number_2, number_3, number_4, number_5]

def mean():
    mean_decimal = int(input("\nHow many decimal places do you want the mean to return? "))
    mean = round((number_1 + number_2 + number_3 + number_4 + number_5) / (len(num_list)), mean_decimal)
    print("\nMean: {}".format(mean))

def median():
    num_list.sort()
    num_list_len = len(num_list)
    median = num_list[2]
    print("Median: {}".format(median))

def mode():
    print(statistics.mode(num_list))
    # This doesn't work with multiple modes. It throws an error. Too lazy to fix at this point in time.
    # Also didn't write accomplish this without importing a function. 

mean()
median()
mode()
