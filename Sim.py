# Library imports
import pygame
import time
import itertools
import numpy as np
import random as rand
import threading as th

# Class imports
import Ant
import Colony

# Decided to build an ant simulation from scratch
## As it is, I need to figure out how to handle the area the ants will run around in
### The current iteration is a cellular automata, so it will be a large 2d array where ants and other objects can
#### only occupy "cells" on a larger grid, but how to represent everything needs to be fleshed out more.

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
