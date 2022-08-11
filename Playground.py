import pygame
import time
import itertools
import numpy as np
import random as rand
import threading as th

# Ant class
class Ant:
    def __init__(self, name, caste) -> None:
        self.name = name
        self.caste = caste
        self.position_x = 0
        self.position_y = 0
        #self.position_z = 0

    def move_rand(self):
        self.position_x = rand.randrange(-10,10,1)
        self.position_y = rand.randrange(-10,10,1)
        #self.position_z = rand.randrange(-10,10,1)

    def move(self, x, y):
        self.position_x += x
        self.position_y += y
        #self.position_z += z

    def position(self):
        return "{}'s position is: ({}, {})".format(self.name, self.position_x, self.position_y)
        #return "{}'s position is: ({}, {}, {})".format(self.name, self.position_x, self.position_y, self.position_z)

class Colony:
    newid = itertools.count().__next__
    def __init__(self, space) -> None:
        self.id = Colony.newid()
        self.locations = np.array((space, space))
        self.ants = []
        print("Colony {} established!".format(self.id))
    
    def ant_add(self, ant):
        self.ants.append(ant)
        print("{} was added to Colony {}".format(ant.name, self.id))
    
    def size(self):
        print("Colony {} has {} ants".format(self.id, len(self.ants)))

class Simulation:
    id = itertools.count().__next__
    def __init__(self, iters):
        self.id = Simulation.id()
        self.iters = iters

# Driver
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

if __name__ == "__main__":
    main()