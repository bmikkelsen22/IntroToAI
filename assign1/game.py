class Shore:
    wolves = 0
    chickens = 0
    boat = False

class Game: 
    # lBoat and rBoat are booleans, others are ints
    def __init__(self, lWolves, lChickens, lBoat, rWolves, rChickens, rBoat):
        self.left = Shore()
        self.right = Shore()

        self.left.wolves = lWolves
        self.left.chickens = lChickens
        self.left.boat = lBoat
        self.right.wolves = rWolves
        self.right.chickens = rChickens
        self.right.boat = rBoat
    
    def ok(self):
        if self.left.chickens < self.left.wolves and self.left.chickens > 0:
            return False
        if self.right.chickens < self.right.wolves and self.right.chickens > 0:
            return False
        if self.left.chickens < 0 or self.left.wolves < 0:
            return False
        if self.right.chickens < 0 or self.right.wolves < 0:
            return False
        return True

def moveChicken(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves, g.left.chickens - 1, False, g.right.wolves, g.right.chickens + 1, True)
    else: #boat starts out on right side
        return Game(g.left.wolves, g.left.chickens + 1, True, g.right.wolves, g.right.chickens - 1, False)

def moveTwoChickens(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves, g.left.chickens - 2, False, g.right.wolves, g.right.chickens + 2, True)
    else: #boat starts out on right side
        return Game(g.left.wolves, g.left.chickens + 2, True, g.right.wolves, g.right.chickens - 2, False)

def moveWolf(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 1, g.left.chickens, False, g.right.wolves + 1, g.right.chickens, True)
    else: #boat starts out on right side
        return Game(g.left.wolves + 1, g.left.chickens, True, g.right.wolves - 1, g.right.chickens, False)

def moveWolfAndChicken(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 1, g.left.chickens - 1, False, g.right.wolves + 1, g.right.chickens + 1, True)
    else: #boat starts out on right side
        return Game(g.left.wolves + 1, g.left.chickens + 1, True, g.right.wolves - 1, g.right.chickens - 1, False)

def moveTwoWolves(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 2, g.left.chickens, False, g.right.wolves + 2, g.right.chickens, True)
    else: #boat starts out on right side
        return Game(g.left.wolves + 2, g.left.chickens, True, g.right.wolves - 2, g.right.chickens, False)
