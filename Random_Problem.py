from Individual import *

class Random_Problem:

    def __init__(self):
        pass

    # Searches for solution to 8-puzzle through random technique
    def random_solve(self, state):
        print("\nSolving Randomly...")

        if state.is_goal():
            print("Root is solution! ", end='')
            state.print_state()
            return

        while not state.is_goal():
            list_of_moves =  self.get_legal_actions(state)

            # Choose a random move from the list of possible moves
            rand_num = randint(0, len(list_of_moves) - 1)
            rand_action = list_of_moves[rand_num]

            state = self.get_new_state(state, rand_action)

        print("Goal Found! ", end='')
        state.print_state()
        return

    # Generate a new state given the old one and an action
    def get_new_state(self, state, action):
        zero_index = self.get_zero_index(state.get_tiles())

        other_tile_index = None
        if action == "UP":
            other_tile_index = zero_index - 3

        if action == "DOWN":
            other_tile_index = zero_index + 3

        if action == "LEFT":
            other_tile_index = zero_index - 1

        if action == "RIGHT":
            other_tile_index = zero_index + 1

        # Swap the tile values at the zero and destination indices
        temp = state.get_tile_at_index(zero_index)
        state.set_tile_at_index(zero_index, state.get_tile_at_index(other_tile_index))
        state.set_tile_at_index(other_tile_index, temp)

        return state

    # Return list of all possible actions from the current state
    def get_legal_actions(self, state):
        list_of_actions = []

        zero_index = self.get_zero_index(state.get_tiles())

        if zero_index == 0:
            list_of_actions.append("RIGHT")
            list_of_actions.append("DOWN")

        if zero_index == 1:
            list_of_actions.append("LEFT")
            list_of_actions.append("RIGHT")
            list_of_actions.append("DOWN")

        if zero_index == 2:
            list_of_actions.append("LEFT")
            list_of_actions.append("DOWN")

        if zero_index == 3:
            list_of_actions.append("UP")
            list_of_actions.append("RIGHT")
            list_of_actions.append("DOWN")

        if zero_index == 4:
            list_of_actions.append("LEFT")
            list_of_actions.append("RIGHT")
            list_of_actions.append("UP")
            list_of_actions.append("DOWN")

        if zero_index == 5:
            list_of_actions.append("LEFT")
            list_of_actions.append("UP")
            list_of_actions.append("DOWN")

        if zero_index == 6:
            list_of_actions.append("UP")
            list_of_actions.append("RIGHT")

        if zero_index == 7:
            list_of_actions.append("LEFT")
            list_of_actions.append("UP")
            list_of_actions.append("RIGHT")

        if zero_index == 8:
            list_of_actions.append("LEFT")
            list_of_actions.append("UP")

        return list_of_actions

    # Find the location of the 'zero' tile
    def get_zero_index(self, tiles):
        zero_index = 0
        for tile in tiles:
            if tile == 0:
                break
            zero_index = zero_index + 1

        return zero_index