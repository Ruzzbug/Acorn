from cells import (
    Air
)

class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0

    def copy(self):
        new_player = Player()
        new_player.num_water_buckets = self.num_water_buckets
        new_player.row = self.row
        new_player.col = self.col
        return(new_player)

    def move(self, move, maze):
        x = self.col
        y = self.row

        if move == 'w':
            self.row -= 1
        elif move == 'a':
            self.col -= 1
        elif move == 's':
            self.row += 1
        elif move == 'd':
            self.col += 1
        elif move == 'e':
            pass

        #Check if the player is trying to move out of bounds or a wall and handle that
        if self.col < 0 or self.row < 0:
            result = False
        else:
            try:
                result = maze[self.row][self.col].step()
            except IndexError:
                result = False
        if result == False:
            self.col = x
            self.row = y
            return f"You walked into a wall. Oof!"
        
        elif result == True:
            return "a"

        elif result == 'W': # Water
            self.num_water_buckets += 1
            maze[self.row][self.col] = Air()
            return "Thank the Honourable Furious Forest, you've found a bucket of water!"

        elif result == 'T': # Teleporter
            tp = maze[self.row][self.col]
            self.row = tp.partner_location[0]
            self.col = tp.partner_location[1]
            return "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."

        elif result == 'F': # Fire 
            if self.num_water_buckets > 0:
                maze[self.row][self.col] = Air()
                self.num_water_buckets -= 1
                return "With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
            else:
                return "dead"

        elif result == 'end':
            return "win"
