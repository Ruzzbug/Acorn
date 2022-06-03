class Start:
    def __init__(self):
        self.display = 'X'

    def step(self):
        return True


class End:
    def __init__(self):
        self.display = 'Y'

    def step(self):
        return 'end'


class Air:
    def __init__(self):
        self.display = ' '

    def step(self):
        return True


class Wall:
    def __init__(self):
        self.display = '*'

    def step(self):
        return False


class Fire:
    def __init__(self):
        self.display = 'F'

    def step(self):
        return 'F'



class Water:
    def __init__(self):
        self.display = 'W'

    def step(self):
        return 'W'


class Teleport:
    def __init__(self, num, y, x): #Teleporters are paired in game_parser()
        self.display = str(num)
        self.location = [y,x]
        self.partner_location = []

    def step(self):
        return 'T'