# Takes a list of lists of cells and converts it to a string to be printed
def grid_to_string(grid, player):
    to_print = ""
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[y])):
            if player.row == y and player.col == x: #Draw the player instead of the cell display
                line += player.display
            else:
                line += grid[y][x].display
        if y == 0:
            to_print += line
        else:
            to_print += "\n" + line
    return to_print
