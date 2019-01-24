from random_word import RandomWords

def find(lst, a):
    result = []
    for i, x in enumerate(lst):
        if x == a:
            result.append(i)
    return result

r = RandomWords()
secret_word = r.get_random_word(maxLength=8).lower()
letter_list = list(secret_word)
dash_list = []
counter = 0

for letter in letter_list:
    dash_list.append('-')


print("Hangman v1.0 - by Matt Kmety\n")
print(" ".join(dash_list) + "\n")
while counter < 6:
    guess = input("\nGuess a letter: ")
    if guess in letter_list:
        indexes = find(letter_list, guess)
        for i in indexes:
            dash_list[i] = guess
            print("\n" + " ".join(dash_list))
        print("That is correct!")
    else:
        if counter == 0:
            print("Incorrect!")
            print(" ------\n |    0\n |\n |\n |\n |\n")
            print("\n" + " ".join(dash_list))
            counter += 1
        elif counter == 1:
            print("Incorrect!")
            counter += 1
            print("\n" + " ".join(dash_list))
            print(" ------\n |     0\n |     |\n |     |\n |\n |\n")
        elif counter == 2:
            print("Incorrect!")
            counter += 1
            print("\n" + " ".join(dash_list))
            print(" ------\n |     0\n |   --|\n |     |\n |\n |\n")
        elif counter == 3:
            print("Incorrect!")
            print("\n" + " ".join(dash_list))
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |\n |\n")
        elif counter == 4:
            print("Incorrect!")
            print("\n" + " ".join(dash_list))
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |    /  \n |\n")
        elif counter == 5:
            print("Incorrect!")
            counter += 1
            print(" ------\n |     0\n |   --|--\n |     |\n |    / \\ \n |\n")
            print("\nYOU LOSE!\nThe word was {}.".format(secret_word))
    combined = "".join(dash_list)
    if combined == secret_word:
        print("You win! The word was {}".format(secret_word))
        break
