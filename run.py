from game import Game
import os
import sys

# Error catching
try:
    maze_file = sys.argv[1]
except IndexError:
    print("No file given!")
    exit()

# Check if the user input play
try:
    mode = sys.argv[2]
except IndexError:
    mode = False

level = Game(maze_file)
if level.error:
    exit()

print(f"{level.grid}\n\nYou have {level.player.num_water_buckets} water buckets.")

first_loop = True

while level.completed == False:
    if first_loop == False:
        print(level.to_print)

    level.to_print = ""
    level.game_move(input("\nInput a move: "))

    if mode == "play":
        os.system('clear')

    first_loop = False
print(level.to_print)
