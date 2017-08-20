"""
Clone of 2048 game.
"""

import poc_2048_gui

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    line2 = [0] * len(line)
    line_index = 0
    for number in range(len(line)):
        if line[number] != 0:
            line2[line_index] = line[number]
            line_index += 1
    for number in range(0, len(line2)):
        if number != len(line2) - 1:
            if line2[number] == line2[number + 1]:
                line2[number] = line2[number] * 2
                line2[number + 1] = 0
    line = [0] * len(line2)
    line_index = 0
    for number in range(len(line2)):
        if line2[number] != 0:
            line[line_index] = line2[number]
            line_index += 1
    return line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = [0]
        self.reset()
        self._upp = [(0, col) for col in range(self.get_grid_width())]
        self._down = [(self.get_grid_height() - 1, col) for col in range(self.get_grid_width())]
        self._left = [(row, 0) for row in range(self.get_grid_height())]
        self._right = [(row, self.get_grid_width() - 1) for row in range(self.get_grid_height())]
        self._initial_tiles = {UP: [self._upp, self.get_grid_height()],
                               DOWN: [self._down, self.get_grid_height()],
                               LEFT: [self._left, self.get_grid_width()],
                               RIGHT: [self._right, self.get_grid_width()]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self.get_grid_width())]
                         for dummy_row in range(self.get_grid_height())]
        
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for row in range(self.get_grid_height()):
            string += "\n"
            for col in range(self.get_grid_width()):
                string += "[" + str(self._grid[row][col]) + "]"
        return string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #This first section computes a list of initial tiles, the required offset
        #and the number of steps that the traverse function is going to use
        initial_tiles = []
        offset = ()
        steps = 0
        for key in self._initial_tiles.keys():
            if direction == key:
                initial_tiles = self._initial_tiles[key][0]
                offset = OFFSETS[key]
                steps = self._initial_tiles[key][1]
        #This creates a temporary list and applies merge
        changes = False
        for initial_tile in initial_tiles:
            temp_list = []
            for step in range(steps):
                row = initial_tile[0] + step * offset[0]
                col = initial_tile[1] + step * offset[1]
                temp_list.append(self._grid[row][col])
            temp_list = merge(temp_list)
            #This passes the temporary list to the actual grid
            for step in range(steps):
                row = initial_tile[0] + step * offset[0]
                col = initial_tile[1] + step * offset[1]
                if self._grid[row][col] != temp_list[step]:
                    changes = True
                self._grid[row][col] = temp_list[step]
        #If there are changes in the grid, create new tile
        if changes:
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_tile_number = random.choice([2] * 9 + [4])
        tile_ready = False
        
        while not tile_ready:
            row_rand = random.randrange(0, self.get_grid_height())
            col_rand = random.randrange(0, self.get_grid_width())
            for row in range(self.get_grid_height()):
                for col in range(self.get_grid_width()):
                    if row == row_rand and col == col_rand and self._grid[row][col] == 0:
                        self._grid[row][col] = new_tile_number
                        tile_ready = True

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

