from random_word import RandomWords

r = RandomWords()
secret_word = r.get_random_word()
secret_word_len = len(secret_word)
secret_word_split = list(secret_word)
counter = 0

print("Hangman v1.0 - by Matt Kmety")
print(secret_word)
print(secret_word_split)
print("__  " * secret_word_len, end="\n")

while counter < 6:
    guess = input("\nGuess a letter: ")
    print(counter)
    if guess in secret_word_split:
        print("Correct!")
    else:
        if counter == 0:
            print("Incorrect!")
            print(" ------\n |     0\n |\n |\n |\n |\n")
            counter += 1
        elif counter == 1:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |     |\n |     |\n |\n |\n")
        elif counter == 2:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |   --|\n |     |\n |\n |\n")
        elif counter == 3:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |\n |\n")
        elif counter == 4:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |    /  \n |\n")
        elif counter == 5:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |    / \\ \n |\n")
            print("\nYOU LOSE!\nThe word was {}.".format(secret_word))

