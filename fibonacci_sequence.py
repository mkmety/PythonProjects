size = int(input("How many numbers in the Fibonacci Sequence do you want to find? "))

counter = 0
num_1 = 0
num_2 = 1

while counter < size:
    print(num_1, end=", ")
    nth = num_1 + num_2
    num_1 = num_2
    num_2 = nth
    counter += 1
