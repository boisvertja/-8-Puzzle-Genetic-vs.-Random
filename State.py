import numpy as numpy

class State:

    def __init__(self, tiles):
        self.tiles = tiles

    # Returns the state's tiles
    def get_tiles(self):
        return self.tiles

    # Sets the state's tiles
    def set_tiles(self, tiles):
        self.tiles = tiles

    # Checks if the current state is equal to the goal state
    def is_goal(self):
        if numpy.array_equal(self.tiles, [1, 2, 3, 4, 5, 6, 7, 8, 0]):
            return True
        return False

    # Print the state
    def print_state(self):
        print(self.tiles)

    # Returns the tile at the given index
    def get_tile_at_index(self, index):
        return self.tiles[index]

    # Sets the value of the tile at the given index
    def set_tile_at_index(self, index, value):
        self.tiles[index] = value