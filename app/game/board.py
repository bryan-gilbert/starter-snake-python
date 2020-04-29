import numpy as np

EMPTY = '.'

class Board:
    def __init__(self, w, h, n):
        self.width = w
        self.height = h
        self.count = n

        # Create a empty board
        emptyCell = [EMPTY] * (1 + self.count)
        row = [emptyCell] * self.width
        col = [row] * self.height
        self.board = np.array( col )

    def getFourLegalPoints(self, x, y):
        results = []
        # down, up, left, and right
        points = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        for p in points:
            if self.inBounds(p[0],p[1]):
                results.append(p)
        return results

    def inBounds(self, x, y):
        return True if x >= 0 and x < self.width and y >= 0 and y < self.height else False

    """ Using col, row order which is the x-axis then the y-axis """

    def set(self, x, y, n, val):
        self.board[y][x][n] = val

    def get(self, x, y, n):
        return self.getAll(x,y)[n]

    def getAll(self, x, y):
        return self.board[y][x]

    def __str__(self):
        text = []
        size = self.count + 1
        row = []
        row.append('{X:^{N}}'.format(X=' ', N=size))
        for x in range(self.width):
            row.append('{X:^{N}}'.format(X=x, N=size))
        text.append(" ".join(row))
        for y, col in enumerate(self.board):
            rowVal = []
            rowVal.append('{X:^{N}}'.format(X=y, N=size))
            for x, row in enumerate(col):
                val = []
                for v in row:
                    val.append('{val}'.format(val=v))
                combined = "".join(val)
                rowVal.append(combined)
            text.append(" ".join(rowVal))
        return "\n".join(text)

