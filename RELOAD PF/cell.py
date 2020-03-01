
class Cell(object):
    FILLED_COLOR_BG = "green"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    def __init__(self, x, y, size, reachable):

        self.reachable = reachable
        self.x = x
        self.y = y
        self.size = size
        self.start = False
        self.end = False
        self.wall = False
        self.weight=1
        self.neighbours = []
        #self.previous=None




    def neigh(self, grid):
        x = self.x
        y = self.y
        if x < 16 - 1:
            self.neighbours.append(grid[x + 1][y])
        if x > 0:
            self.neighbours.append(grid[x - 1][y])
        if y < 16 - 1:
            self.neighbours.append(grid[x][y + 1])
        if y > 0:
            self.neighbours.append(grid[x][y - 1])
            # diagonals
        # if x > 0 and y > 0:
        #     self.neighbours.append(grid[x - 1][y - 1])
        #
        # if x < 8 - 1 and y > 0:
        #     self.neighbours.append(grid[x + 1][y - 1])
        #
        # if x > 0 and y < 8 - 1:
        #     self.neighbours.append(grid[x - 1][y + 1])
        #
        # if x < 8 - 1 and y < 8 - 1:
        #     self.neighbours.append(grid[x + 1][y + 1])





    def __lt__(self, tile2):
        """
        "Less than" for comparing two tile's weight.
        :param tile2:
        :return:
        """
        #compares weithgt for priority queque when the have the same priority to choose the least
        return self.weight < tile2.weight







