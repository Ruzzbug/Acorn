from solver import(solve)
from game import Game
import sys
import os
#  import time # Just looks better with a pause between each move, but it's not allowed in submission

#Make sure that a maze file and a method are given
try:
    maze_file = sys.argv[1]
except IndexError:
    print("No file given!")
    exit()
try:
    mode = sys.argv[2]
except IndexError:
    print("No solve method given!")
    exit()

 # Set up the initial gamestate for solve()

auto_sol = solve(maze_file, mode) # Run bfs or dfs and assign result to auto_sol

if auto_sol == False:
    print("No possible solution.")
    exit()

level = Game(maze_file) # Reset gamestate for the player emulator

#Play the game like a player would with inputs from auto_sol
i = 0
while level.completed == False:      
    print(level.to_print)
    level.to_print = ""
    level.game_move(auto_sol[i])
    # time.sleep(0.1)
    os.system('clear')
    i += 1
print(level.to_print)
exit()