from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

#Pairs the teleporters so that they reference their partners
def pair_teleporters(teleporters):
    test_arr = teleporters

    for x in range(len(teleporters)):
            for y in range(x + 1, len(teleporters)):
                if teleporters[x].display == teleporters[y].display and teleporters[y].partner_location == []:
                    teleporters[x].partner_location = teleporters[y].location
                    teleporters[y].partner_location = teleporters[x].location
    
    # Missing a partner
    try:
        for i in teleporters:
            if i.partner_location == []:
                raise ValueError
    except ValueError:
        print(f"Teleport pad {i.display} does not have an exclusively matching pad.")
        return False


#Turn list of strings into list of cells
def parse(lines):
    err_msg = ""
    
    starts = 0
    ends = 0
    teleporters = []
    maze = []

    # Optimise the file for conversion to cells
    for i in range(len(lines)):
            maze.append([])
            for x in lines[i]:
                if x != "\n":
                    maze[i].append(x)
                    
    cell_dictionary = {
    " ": Air(),
    "*": Wall(),
    "W": Water(),
    "F": Fire(),
    "X": Start(),
    "Y": End()  
    }

    tele_display = []
    # Convert string items into cells
    for y in range(len(maze)):
        i = 0
        for x in maze[y]:
            if x in cell_dictionary:
                if maze[y][i] == "X":
                    starts += 1
                elif maze[y][i] == "Y":
                    ends += 1
                maze[y][i] = cell_dictionary.get(x)
            else:
                try:
                    maze[y][i] = int(x)
                    if maze[y][i] <= 0:
                        raise ValueError
                    tele_display.append(x)
                    if tele_display.count(x) > 2:
                        print(f"There are 3 or more of Teleporter {x}.")
                        return False
                    maze[y][i] = Teleport(x, y, i)
                    teleporters.append(maze[y][i]) # Add to the teleporters list so they can be paired
                except TypeError:
                    print("Bad maze file\nI'm surprised you were able to get this error to show, congratulations.")
                    return False
                except ValueError:
                    print(f"Bad letter in configuration file: {(y, i)}.")
                    return False
            i += 1

    # Error catching
    try:
        if starts != 1 or ends != 1:
            raise ValueError
    except ValueError:
        if starts != 1:
            print(f"Expected 1 starting position, got {starts}.")
            return False
        if ends != 1:
            print(f"Expected 1 ending position, got {ends}.")
            return False
    if pair_teleporters(teleporters) == False:
        return False
    return (maze)
    
# Reads the lines and sends them to parse as a string before returning a list of cells from parse
def read_lines(maze_file):
    ls = []
    try:
        with open(maze_file, "r") as f:
            ls = f.readlines()
    except OSError:
        print(f"{maze_file} does not exist!")
        exit()
    return (parse(ls))



