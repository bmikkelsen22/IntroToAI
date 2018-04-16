class Shore:
    wolves = 0
    chickens = 0
    boat = False

class Game: 
    # lBoat and rBoat are booleans, others are ints
    def __init__(self, lWolves, lChickens, lBoat, rWolves, rChickens, rBoat, pred = None):
        self.left = Shore()
        self.right = Shore()
        self.pred = pred
        self.depth = pred.depth + 1 if pred else 0

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

    def __eq__(self, other):
        if self.left.wolves != other.left.wolves:
            return False
        if self.left.chickens != other.left.chickens:
            return False
        if self.left.boat != other.left.boat:
            return False
        if self.right.wolves != other.right.wolves:
            return False
        if self.right.chickens != other.right.chickens:
            return False
        if self.right.boat != other.right.boat:
            return False
        return True
    
    def __hash__(self):
        h = self.left.wolves * 10 + self.left.chickens * 1000
        h += self.right.wolves * 100000 + self.right.chickens * 10000000
        if self.left.boat:
            h += 1
        return h

    def __str__(self):
        leftBoat = "boat" if self.left.boat else "no boat"
        rightBoat = "boat" if self.right.boat else "no boat"
        predString = str(self.pred) if self.pred else ""

        return "%s%d wolves, %d chickens, %s | %d wolves, %d chickens, %s\n" % (predString, self.left.wolves, self.left.chickens, leftBoat, self.right.wolves, self.right.chickens, rightBoat)
        
        

def moveChicken(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves, g.left.chickens - 1, False, g.right.wolves, g.right.chickens + 1, True, g)
    else: #boat starts out on right side
        return Game(g.left.wolves, g.left.chickens + 1, True, g.right.wolves, g.right.chickens - 1, False, g)

def moveTwoChickens(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves, g.left.chickens - 2, False, g.right.wolves, g.right.chickens + 2, True, g)
    else: #boat starts out on right side
        return Game(g.left.wolves, g.left.chickens + 2, True, g.right.wolves, g.right.chickens - 2, False, g)

def moveWolf(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 1, g.left.chickens, False, g.right.wolves + 1, g.right.chickens, True, g)
    else: #boat starts out on right side
        return Game(g.left.wolves + 1, g.left.chickens, True, g.right.wolves - 1, g.right.chickens, False, g)

def moveWolfAndChicken(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 1, g.left.chickens - 1, False, g.right.wolves + 1, g.right.chickens + 1, True, g)
    else: #boat starts out on right side
        return Game(g.left.wolves + 1, g.left.chickens + 1, True, g.right.wolves - 1, g.right.chickens - 1, False, g)

def moveTwoWolves(g):
    if g.left.boat: #boat starts out on left side
        return Game(g.left.wolves - 2, g.left.chickens, False, g.right.wolves + 2, g.right.chickens, True, g)
    else: #boat starts out on right side
        return Game(g.left.wolves + 2, g.left.chickens, True, g.right.wolves - 2, g.right.chickens, False, g)
