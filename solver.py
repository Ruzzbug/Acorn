from game import Game
import os
import sys
from cells import (End, Teleport)

class Solver:
    def __init__(self, game_state):
        self.level = game_state
        self.visited = []

    def copy(self):
        new_state = Solver(self.level.copy()) # Makes new solver object with copied gamestate with copied player
        new_state.visited = self.visited # References the parent array (doesn't copy)
        return new_state  


def solve(maze_file, mode):
    mode = str.upper(mode)
    state = Solver(Game(maze_file))
    options = [['a', (0, -1)], ['d', (0, 1)], ['s', (1, 0)], ['w', (-1, 0)], ['e', (0, 0)]]
    frontier = []
    state.visited.append((state.level.player.row, state.level.player.col))
    frontier.append(state)
    while len(frontier) > 0:
        if mode == 'BFS': #BFS uses a queue
            state = frontier.pop(0)
        elif mode == 'DFS': #DFS uses a stack
            state = frontier.pop()
        for move in options:
            y = state.level.player.row + move[1][0]
            x = state.level.player.col + move[1][1]
            try:
                cell = state.level.maze[y][x].display
            except IndexError:
                state.visited.append((y, x))
            if cell != "" and cell != "*" and (y, x) not in state.visited:
                new_state = state.copy()  # Copy to get a new game instance instead of just a reference to state
                result = new_state.level.game_move(move[0])
                if result == "Thank the Honourable Furious Forest, you've found a bucket of water!":
                    new_state.visited = [] # Create a new visited list because the parent visited is no longer relevant to this game state
                new_state.visited.append((y, x))
                if result == "dead":
                    pass
                elif result == "win": 
                    return new_state.level.moves
                else:
                    frontier.append(new_state)
    return(False)


if __name__ == "__main__":
    maze_file = sys.argv[1]
    mode = sys.argv[2]
    result = (solve(maze_file, mode))
    if result == False:
        print("There is no possible path.")
        exit()
    else:
        if len(result) != 1:
            opt_s = "s"
        else:
            opt_s = ""
        print(f"Path has {len(result)} move{opt_s}.\n" +\
        f"Path: {', '.join(result)}")
                            