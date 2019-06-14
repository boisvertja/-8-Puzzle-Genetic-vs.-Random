from Genetic_Problem import *
from Random_Problem import *

if __name__ == "__main__":
    # Solve with genetic algorithm
    gp = Genetic_Problem(100)
    gp.genetic_algorithm()

    # Solve by choosing random actions
    rand = Random_Problem()
    state = State([7, 2, 4, 5, 0, 6, 8, 3, 1])
    rand.random_solve(state)
