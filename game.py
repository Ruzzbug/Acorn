from game_parser import read_lines
from grid import grid_to_string
from player import Player
import os


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.completed = False
        self.player = Player()
        self.maze = read_lines(filename)
        self.moves = ""
        self.error = False
        
        # Handles the errors from game_parser so that the test program doesn't exit
        if self.maze == False:
            self.error = True
            return

        # Sets the player's starting position
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x].display == 'X':
                    self.player.row = y
                    self.player.col = x
                    break

        self.grid = grid_to_string(self.maze, self.player)
        self.to_print = self.grid # self.to_print is appended with everything that will be printed. It cleared in run.py
        

    # Copies the game
    def copy(self):
        new_game = Game(self.filename)
        new_game.maze = [row[:] for row in self.maze]
        new_game.player = self.player.copy() # Copies the player
        new_game.moves = self.moves
        return new_game

    # Updates the grid again and builds the self.to_print variable
    def step(self, output):
        self.grid = grid_to_string(self.maze, self.player)
        self.to_print += self.grid

        #  water bucket(s)
        if self.player.num_water_buckets == 1:
            s = ''
        else:
            s = 's'
        self.to_print += f"\n\nYou have {self.player.num_water_buckets} water bucket{s}."

        if output == "dead" or output == "win":
            self.completed = True

            # Adds an "s" if there was more than one move
            if len(self.moves) > 1:
                opt_s = "s"
            else:
                opt_s = ""

        if output == "dead":
            self.to_print +="\n\n\nYou step into the fires and watch your dreams disappear :(."
            self.to_print += "\n\nThe Fire Nation triumphs! " +\
                             "The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... " +\
                             "You have been roasted.\n" +\
                             f"\nYou made {len(self.moves)} move{opt_s}.\n" +\
                             f"Your move{opt_s}: {', '.join(self.moves)}\n" +\
                             "\n=====================\n===== GAME OVER =====\n====================="

        elif output == "win":
            self.to_print += f"\n\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the " +\
                                "Honourable Furious Forest Throne, restoring your hometown back to its former " +\
                                "glory of rainbow and sunshine! Peace reigns over the lands.\n" +\
                                f"\nYou made {len(self.moves)} move{opt_s}.\n" +\
                                f"Your move{opt_s}: {', '.join(self.moves)}\n" +\
                                "\n=====================\n====== YOU WIN! =====\n====================="

        elif output != "":
            self.to_print += f"\n\n{output}"
        return output
        

    # passes input to player and handles immediate response
    def game_move(self, move):
        move = move.lower()
        if move == 'w' or move == 'a' or move == 's' or move == 'd' or move == 'e':
            self.moves += move 
            output = self.player.move(move, self.maze)
            if output == 'a':
                output = ""
            self.step(output)
            if output == "You walked into a wall. Oof!": 
                self.moves = self.moves[:-1] #remove the input that drove them into the wall
            return output
        elif move == 'q':
            print("\nBye!")
            exit()
        else:
            self.step("")
            self.to_print += "\n\nPlease enter a valid move (w, a, s, d, e, q)."
   
