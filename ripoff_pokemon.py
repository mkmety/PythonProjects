import random

print("Welcome to the rip-off version of Pokemon\n")

player_character_name = input("Enter your bad-ass character name: ")
enemy_character_name = "Russ"

player_hit_points = 100
enemy_hit_points = 100

move_one_name = "Shank"
move_one_desc = "You attempt to shank " + enemy_character_name + "."
move_one_miss_desc = "You missed your shank attempt."

move_two_name = "Roundhouse"
move_two_desc = "You attempt to roundhouse " + enemy_character_name + "."
move_two_miss_desc = "You missed terribly.."

move_three_name = "Heal"

while player_hit_points > 0 and enemy_hit_points > 0:
    move_one_accuracy = random.randint(1, 11)
    move_one_damage = random.randint(18, 26)
    move_one_hit_desc = "You shanked his ass for {}.".format(move_one_damage)
    move_two_accuracy = random.randint(1, 11)
    move_two_damage = random.randint(10, 36)
    move_two_hit_desc = "You roundhoused {} in the face for {}!".format(enemy_character_name, move_two_damage)

    print("\n" + player_character_name + ", choose your next move.")
    print("\nShank\nRoundhouse\nHeal")
    next_move = input("\nEnter Move: ")
    if next_move == "Shank":
        print(move_one_desc)
        if move_one_accuracy > 3:
            print(move_one_hit_desc)
            enemy_hit_points = enemy_hit_points - move_one_damage
            if enemy_hit_points < 0:
                enemy_hit_points = 0
                print("{} has been killed. You win!".format(enemy_character_name))
            print("{} has {} hit points left.".format(enemy_character_name, enemy_hit_points))
        else:
            print(move_one_miss_desc)
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))
    elif next_move == "Roundhouse":
        print(move_two_desc)
        if move_two_accuracy > 4:
            print(move_two_hit_desc)
            enemy_hit_points = enemy_hit_points - move_two_damage
            if enemy_hit_points < 0:
                enemy_hit_points = 0
                print("{} has been killed. You win!".format(enemy_character_name))
            print("{} has {} hit points left.".format(enemy_character_name, enemy_hit_points))
        else:
            print(move_two_miss_desc)
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))
    elif next_move == "Heal":
        if player_hit_points < 76:
            player_hit_points = player_hit_points + 25
            print(("You heal yourself for 25."))
            print("Your HP is now {}".format(player_hit_points))
        elif player_hit_points > 75 and player_hit_points < 100:
            player_hit_points = 100
            print("You healed yourself to max health")
            print("Your HP is now {}".format(player_hit_points))
        elif player_hit_points == 100:
            print("You were already at full health. You hurt yourself in confusion")
            player_hit_points = player_hit_points - 5
            print("Your HP is now {}".format(player_hit_points))
    print("\n{} attacks you for 1,000,000. You are fucking dead.".format(enemy_character_name))
    player_hit_points = 0


