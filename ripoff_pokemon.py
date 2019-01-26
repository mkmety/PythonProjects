import random

print("Welcome to the rip-off version of Pokemon")

player_character_name = input("Enter your character name: ")
enemy_character_name = "Russ"

player_hit_points = 100
enemy_hit_points = 100

move_one_name = "Shank"
move_one_desc = "You attempt to shank " + enemy_character_name + "."
move_one_accuracy = random.randint(1, 11)
move_one_damage = random.randint(18, 26)
move_one_hit_desc = "You shanked his ass for {}.".format(move_one_damage)
move_one_miss_desc = "You missed your shank attempt."

move_two_name = "Roundhouse"
move_two_desc = "You attempt to roundhouse " + enemy_character_name + "."
move_two_accuracy = random.randint(1, 11)
move_two_damage = random.randint(10, 36)
move_two_hit_desc = "You roundhoused " + enemy_character_name + " in the face!"
move_two_miss_desc = "You missed terribly.."

move_three_name = "Heal"
move_three_desc = "You heal yourself."
move_three_accuracy = 100
move_two_healing = -25

while player_hit_points > 0 and enemy_hit_points > 0:
    move_one_accuracy = random.randint(1, 11)
    move_one_damage = random.randint(18, 26)
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
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))
        else:
            print(move_one_miss_desc)
            print("{} has {} left.".format(enemy_character_name, enemy_hit_points))


