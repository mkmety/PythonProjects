print("Welcome to the Pythagorean Triples Checker! \n\n"
      "You will need to enter in the 3 sides of a triangle to see if the triangle is Pythagorean Triple \n")
play_again = True

while play_again:
    side_1 = int(input("Enter first length of one side of a triangle: "))
    side_2 = int(input("Enter second length of one side of a triangle: "))
    side_3 = int(input("Enter third length of one side of a triangle: "))

    side_list = [side_1, side_2, side_3]
    side_list.sort()

    if side_list[0] ^ 2 + side_list[1] ^ 2 == side_list[2] ^ 2:
        print("\nThis is a Pythagorean Triple Triangle")
    else:
        print("\nThis is not a Pythagorean Triple Triangle")
    play_again_input = input("\nWould you like to try another? (Yes or No)")
    if play_again_input == "Yes":
        play_again = True
    elif play_again_input == "No":
        play_again = False
    else:
        play_again = False
        print("\nInvalid Choice")
