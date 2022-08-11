import pygame
import time
import itertools
import numpy as np
import random as rand
import threading as th

# Decided to build an ant simulation from scratch
## As it is, I need to figure out how to handle the area the ants will run around in
### The current iteration is a cellular automata, so it will be a large 2d array where ants and other objects can
#### only occupy "cells" on a larger grid, but how to represent everything needs to be fleshed out more.

# Ant class
class Ant:
    def __init__(self, name, caste) -> None:
        self.name = name
        self.caste = caste
        self.position_x = 0
        self.position_y = 0
        self.speed = rand.randrange(1,5)
        #self.position_z = 0

    # Ant moves randomly with no directional bias
    def move_rand(self):
        old_x = self.position_x
        old_y = self.position_y
        self.position_x += rand.randrange(-1 * self.speed, * self.speed, 1)
        self.position_y += rand.randrange(-1 * self.speed, * self.speed, 1)
        #self.position_z = rand.randrange(-10,10,1)
        print("{} has moved from ({}, {}) to ({}, {})".format(self.name, old_x, old_y, self.position_x, self.position_y))

    def move(self, x, y):
        self.position_x += x
        self.position_y += y
        #self.position_z += z

    def position(self):
        return "{}'s position is: ({}, {})".format(self.name, self.position_x, self.position_y)
        #return "{}'s position is: ({}, {}, {})".format(self.name, self.position_x, self.position_y, self.position_z)

# Colony for the ants, acts as a structure but also will allow for multiple colonies in a sim
class Colony:
    newid = itertools.count().__next__
    # max number of ants
    def __init__(self, space) -> None:
        self.id = Colony.newid()
        self.ants = []
        self.space = space
        print("Colony {} established!".format(self.id))
    
    def ant_add(self, ant):
        self.ants.append(ant)
        print("{} was added to Colony {}".format(ant.name, self.id))
    
    def size(self):
        print("Colony {} has {} ants".format(self.id, len(self.ants)))

class Cell:
    def __init__(self) -> None:
        self.ants = []

# Handles the update for the ants and colonies
class Simulation:
    id = itertools.count().__next__
    # number of iterations, time step per update
    def __init__(self, area, iters, step):
        self.id = Simulation.id()
        self.area = np.zeros((area, area))
        self.iters = iters
        self.colonies = []
        self.step = step
        self.curr = 0

    # Add a colony to the list of colonies
    def add_colony(self, c):
        self.colonies.append(c)
        for ant in c.ants:
            x = ant.position_x
            y = ant.position_y
            self.area[x][y] = self.area[x][y] + 1

    # Update the step in the simulation
    def update(self):
        print("step {}".format(self.curr))

        for c in self.colonies:
            for ant in c.ants:
                x = ant.position_x
                y = ant.position_y
                self.area[x][y] = self.area[x][y] - 1
                ant.move_rand()

        curr += 1


# Driver for the sim
def main():
    timmy = Ant("Timothy", "worker")
    jimmy = Ant("Jimothy", "soldier")

    # string format
    print("Say hello to {}!".format(timmy.name))
    print("{} is a {} ant.".format(timmy.name, timmy.caste))

    print("Say hello to {}!".format(jimmy.name))
    print("{} is a {} ant.".format(jimmy.name, jimmy.caste))

    cleveland = Colony(1000)
    cleveland.ant_add(timmy)
    cleveland.ant_add(jimmy)
    cleveland.size()

    sim1 = Simulation(10000, 10000, 0.1)
    sim1.add_colony(cleveland)
    print(sim1.area)

if __name__ == "__main__":
    main()
