from State import *
from random import randint

class Individual:

    def __init__(self):
        # Initialize random state
        temp = []

        # Populate state with random sequence of distinct numbers 0 - 8
        while not len(temp) == 9:
            rand = randint(0, 8)
            while rand in temp:
                rand = randint(0, 8)
            temp.append(rand)

        self.state = State(numpy.array(temp))

    # Returns the number of correctly positioned tiles in the current state
    def fitness(self):
        goal_state = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
        num_same = numpy.sum(goal_state == self.get_state().get_tiles())
        return num_same

    # Returns the individual's state
    def get_state(self):
        return self.state