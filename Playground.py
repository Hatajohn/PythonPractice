import pygame

# Ants
class Ant:
    caste = ""
    def __init__(self, name, caste) -> None:
        self.name = name
        self.caste = caste

# Driver

timmy = Ant("Timothy", "worker")
print("Say hello to {}!".format(timmy.name))
print("{} is a {} ant.".format(timmy.name, timmy.caste))