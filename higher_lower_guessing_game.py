import random

print("Welcome to the number guessing game or whatever..")
print("Guess a number between 1 and 100. The program will tell you if the number is higher or lower and you"
      "can guess again until you get it right! ")


def rando():
    for x in range(1):
        return(random.randint(1, 101))


secret_number = rando()
guess = ""
count = 0
play_again = True

while (guess != secret_number) and (play_again == True):
    guess = int(input("\nGuess a number: "))
    count += 1
    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print("You guessed the number correctly! Congrats! \nIt took you {} guesses".format(count))
        play_again = input("Would you like to play again? ")
        if play_again == "Yes":
            play_again = True
            guess = ""
            secret_number = rando()
            count = 0
        elif play_again == "No":
            print("Thanks for playing!")
            play_again = False
        else:
            print("Not a valid response")
            play_again = False
