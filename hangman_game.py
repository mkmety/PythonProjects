from random_word import RandomWords


r = RandomWords()
secret_word = r.get_random_word().lower()
counter = 0
word_guessed = []

for letter in secret_word:
            word_guessed.append("-")


print("Hangman v1.0 - by Matt Kmety")
print(secret_word)

while counter < 6:
    print(word_guessed)
    guess = input("\nGuess a letter: ")
    for letter in range(len(secret_word)):
        if guess == secret_word[letter]:
            word_guessed[letter] = guess
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

