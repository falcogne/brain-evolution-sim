import random
from PIL import Image
import numpy as np

from board import Board
from player import Player
from brain import Brain
import constants

IMAGES_DICT = 'run_1'

NUM_PLAYERS = constants.NUM_PLAYERS

class Environment():
    def __init__(self):
        self.board = Board(constants.SIZE)
        self.players = []
        for _ in range(NUM_PLAYERS):
            position = [
                random.randint(0, constants.SIZE[0]-1),
                random.randint(0, constants.SIZE[1]-1)
            ]
            # print(position)
            self.players.append(
                Player(position, Brain(), self.board)
            )
    
    
    def pixel_rep(self):
        base_pix = self.board.pixel_rep()
        for p in self.players:
            base_pix[p.position[1]][p.position[0]] = constants.PLAYER_COLOR
        return base_pix
    

    def step(self):
        to_remove = []

        for p in self.players:
            window, possible_moves = self.board.window(loc=p.position, dist=p.vision)
            possible_moves.append(('harvest',))
            possible_moves.append(('eat', 10))
            p.set_window(window)
            alive = p.take_action(possible_moves)
            if not alive:
                to_remove.append(p)

        for p in to_remove:
            self.players.remove(p)

        
    
    def sim(self, steps=10):
        n = 0
        # for s in range(steps):
        while len(self.players) > 0:
            self.step()
            pix = self.pixel_rep()
            self.render_environment(pix, str(n))
            n += 1
    
    def render_environment(self, pixels, step=""):
        array = np.array(pixels, dtype=np.uint8)
        image = Image.fromarray(array)
        image.save(f"{IMAGES_DICT}/env{step}.png")
        # image.show("environment state")


if __name__ == "__main__":
    env = Environment()
    env.sim()