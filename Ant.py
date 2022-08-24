import random as rand
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