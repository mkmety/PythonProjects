import random

print("Welcome to the rip-off version of Pokemon")

#player_character_name = input("Enter your character name: ")
enemy_character_name = "Russ"

player_hit_points = 100
enemy_hit_points = 100

move_one_name = "Shank"
move_one_desc = "You attempt to shank " + enemy_character_name + "."
move_one_accuracy = random.randint(70, 101)
move_one_damage = random.randint(18-26)
move_one_hit_desc = "You shanked his ass."
move_one_miss_desc = "You missed your shank attempt."

move_two_name = "Roundhouse"
move_two_desc = "You attempt to roundhouse " + enemy_character_name + "."
move_two_accuracy = random.randint(60, 101)
move_two_damage = random.randint(10-36)
move_two_hit_desc = "You roundhoused " + enemy_character_name + " in the face!"
move_two_miss_desc = "You missed terribly.."

move_three_name = "Heal"
move_three_desc = "You heal yourself."
move_three_accuracy = 100
move_two_healing = -25
