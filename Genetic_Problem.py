# Pseudocode for tournament selection used from 'https://stackoverflow.com/questions/31933784/tournament-selection-in-genetic-algorithm'
# Code for swapping elements in array used from 'https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa'
from Individual import *
from random import uniform

class Genetic_Problem:

    MUTATION_PROB = 0.8 # 40% chance of mutation

    def __init__(self, population_size):
        self.population = []
        for i in range(0, population_size):
            self.population.append(Individual())

        # Keep track of previous champion so selection algorithm doesn't just keep choosing the same parent for everything
        self.previous_champion = Individual()

    # Searches for solution to 8-puzzle through fitness-ad-hoc technique
    def genetic_algorithm(self):
        print("Solving Genetically...")

        while True:
            # Check if some individual in population is goal state
            for individual in self.population:
                if individual.get_state().is_goal():
                    print("Goal Found! ", end='')
                    individual.get_state().print_state()
                    return

            new_population = []
            for i in range(0, len(self.population) - 1):
                # Acquire the most fit individual in the population
                x = self.selection(self.population)
                y = self.selection(self.population)

                # Create child and mutate if small probability determines
                child = self.crossover(x, y)

                if randint(0, 20) == 13:
                    child = self.mutate(child)

                new_population.append(child)

            self.population = new_population[:]

            if len(self.population) == 0:
                print("ERROR::POPULATION_IS_EMPTY")
                print("Best so far: ", end='')
                x.get_state().print_state()
                return

    # Randomly crossover a few tiles if pseudo-randomness deems the individuals worthy
    def crossover(self, x, y):
        set_y = y.get_state().get_tiles()
        set_x = x.get_state().get_tiles()

        child = Individual()
        child.get_state().set_tiles(set_y)

        # Ensure the new state only contains distinct numbers
        new_state = [-1, -1]
        while not self.distinct(new_state):
            crossover_point = randint(1, 9)

            y_partial = set_y[0:crossover_point]
            x_partial = set_x[crossover_point:9]

            # Combine the two partials into a new state
            new_state = numpy.concatenate((y_partial, x_partial))

        child.get_state().set_tiles(new_state)
        return child

    # Randomly mutates tiles in the child's state ensuring that each is distinct
    def mutate(self, child):
        # Each tile has a specified probability of being mutated
        set = child.get_state().get_tiles()
        for tile in set:
            rand_mutation = uniform(0, 1)
            if rand_mutation >= Genetic_Problem.MUTATION_PROB:

                # Generate a new random tile value
                new_tile = randint(0, 8)

                # Locate the index of the newly generated value already in the list
                new_tile_index = self.find_tile_index(set, new_tile)
                current_tile_index = self.find_tile_index(set, tile)

                # Swap the 'new_tile' with the tile in the 'new_tile's current index in the set
                set[new_tile_index], set[current_tile_index] = set[current_tile_index], set[new_tile_index]

        return child

    # Returns the most fit individual in the population
    def selection(self, population):
        best = None
        for individual in population:
            if best == None or individual.fitness() >= best.fitness() and not best == self.previous_champion:
                best = individual

        # Update previous champion
        self.previous_champion = best
        return best

    # Returns index of 'tile' in 'set', nothing if not found
    def find_tile_index(self, set, tile):
        index = 0
        for el in set:
            if el == tile:
                return index
            index = index + 1

        print("ERROR::TILE_INDEX_VALUE_NOT_FOUND")
        return

    # Ensures that each child has only distinctly-numbered tiles
    def distinct(self, set):
        seen = []
        for tile in set:
            if tile in seen:
                return False
            seen.append(tile)
        return True