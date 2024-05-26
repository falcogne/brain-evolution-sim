import numpy as np
import random
import constants

class Board():
    def __init__(self, size):
        self.squares = np.array(
            [
                [
                    Location(
                        traversal_cost=random.randint(0, 1),
                        max_food=random.randint(0, 10),
                        fertility=random.random()
                    )
                    for _ in range(constants.SIZE[0])
                ]
                for _ in range(constants.SIZE[1])
            ]

        )
    
    def player_rep(self):
        b = Board((1,1))
        b.squares = np.copy(self.squares)
        # b.squares = self.squares.copy()

    def pixel_rep(self):
        pix = []
        for row in self.squares:
            pix.append([])
            for loc in row:
                pix[-1].append(loc.pixel_value())
        return pix

    def window(self, loc, dist):
        w = []
        moves = []
        for y in range(loc[1]-dist, loc[1]+dist+1):
            arr = []
            for x in range(loc[0]-dist, loc[0]+dist+1):
                try:
                    arr.append(self.squares[y][x])
                    if self.squares[y][x].valid and abs(x-loc[0]) <= 1 and abs(y-loc[1]) <= 1:
                        moves.append(('move',x,y))
                except IndexError:
                    invalid = Location(valid=False)
                    invalid.valid = False
                    arr.append(invalid)
            w.append(arr)
        return w, moves

    def harvest(self, loc):
        return self.squares[loc[1]][loc[0]].harvest()

class Location():
    def __init__(self, traversal_cost=0, max_food=0, food=None, fertility=0, valid=True, seen=False,):
        self.valid = valid
        self.seen = seen
        self.traversal_cost = traversal_cost
        self.max_food = max_food
        if food is None:
            self.food = random.randint(0, max_food)
        else:
            self.food = food
        self.fertility = fertility
        # self.irrigation
        # self.flatness
    
    def pixel_value(self):
        norm_cost = min(self.traversal_cost / constants.MAX_PLAYER_ENERGY, 1)
        norm_fertility = self.fertility
        
        # Determine darkness based on cost (0 to 255)
        # darkness = int((1 - norm_cost) * 255)
        
        # Base colors for grass-like green and sand-like yellow
        grass_green = (34, 139, 34)
        sand_yellow = (210, 180, 140)
        
        # Interpolate between grass-green and sand-yellow based on fertility
        if norm_fertility > 0.5:
            # High fertility: More green
            red = int(grass_green[0] * norm_fertility)
            green = int(grass_green[1] * norm_fertility)
            blue = int(grass_green[2] * norm_fertility)
        else:
            # Low fertility: More yellow
            red = int(sand_yellow[0] * (1 - norm_fertility))
            green = int(sand_yellow[1] * (1 - norm_fertility))
            blue = int(sand_yellow[2] * (1 - norm_fertility))
        
        # Apply darkness to the RGB values
        red = int(red * (1 - norm_cost))
        green = int(green * (1 - norm_cost))
        blue = int(blue * (1 - norm_cost))
        
        return (red, green, blue)
    
    def __copy__(self):
        l = Location(
            valid=self.valid,
            seen=self.seen,
            traversal_cost=self.traversal_cost,
            max_food=self.max_food,
            food=self.food,
            fertility=self.fertility,

        )
        return l
    
    def harvest(self):
        f = self.food
        self.food = 0
        return f

    def step(self):
        self.food += self.fertility
        if self.food > self.max_food:
            self.food = self.max_food
    