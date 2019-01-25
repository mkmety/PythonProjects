import random
from collections import Counter

dice_size = int(input("What sided dice would you like to throw? "))
times_thrown = int(input("How many times would you like to throw the dice?"))
count = 0
results_list = []

while count < times_thrown:
    result = random.randint(1, dice_size)
    results_list.append(result)
    count += 1
counter_list = Counter(results_list)

print("Number     Frequency     %")
print("--------------------------")

for dice in counter_list:
    print("{:3}         {:3}       {:3}%".format(dice, counter_list[dice], round((counter_list[dice] / times_thrown) * 100, 4)))
