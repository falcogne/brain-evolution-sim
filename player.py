import random
import constants

class Player():
    def __init__(self, position, brain, init_board):
        # self.age = 0
        self.breedable = True
        self.energy = constants.MAX_PLAYER_ENERGY
        self.held_food = 0
        self.alive = True
        self.position = position
        self.brain = brain
        self.vision = 2
        self.window = None
        self.board_obj = init_board
        self.board_vision = init_board.player_rep()


    def use_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.alive = False
        return self.alive

    def eat_food(self, amount):
        most_can_eat = min(constants.MAX_PLAYER_ENERGY-self.energy, self.held_food)
        if amount > most_can_eat:
            print(f"can't eat that much, only gonna eat {most_can_eat}")
            self.energy += most_can_eat
            self.held_food -= most_can_eat
            # return most_can_eat
        else:
            self.energy += amount
            self.held_food -= amount
            # return amount
        return self.use_energy(constants.EAT_ENERGY)
    
    def set_window(self, window):
        self.window = window
        # TODO: overlay onto total board memory?

    def move(self, move):
        self.position = move
        return self.use_energy(constants.MOVE_ENERGY)
    
    def harvest(self):
        food = self.board_obj.harvest(self.position)
        self.held_food += food
        return self.use_energy(constants.HARVEST_ENERGY)

    def take_action(self, possible_moves):
        decision = self.brain.make_decision(possible_moves)
        if decision[0] == 'move':
            return self.move((decision[1], decision[2]))
        elif decision[0] == 'harvest':
            return self.harvest()
        elif decision[0] == 'eat':
            return self.eat_food(decision[1])


