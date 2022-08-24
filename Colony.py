import itertools
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