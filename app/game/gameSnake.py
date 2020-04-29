import string

EMPTY = '.'
BLOCKED = ':'
class Analysis:
    count = 0
    def __str__(self):
        b = str(self.count)
        return '{}'.format(b)

class GameSnake:
    def __init__(self, id, index, body):
        self.id = id
        self.index = index
        self.body = body
        self.move = None
        self.shout = None
        # Z, T, X, W ....
        self.letters = (string.ascii_uppercase[::-1])[:len(self.body)]

    def getLength(self):
        return len(self.body)

    def floodHead(self, board, stepLimit):
        self.stepLimit = stepLimit # save for analysis
        head = self.body[0]
        x = head[0]
        y = head[1]

        next = board.getFourLegalPoints(x, y)
        start = 0
        for pt in next:
            floodFrom(self.index, board, pt, start, stepLimit)

    def addBodyToBoard(self, board):
        n = self.index
        for i, pt in enumerate(self.body):
            board.set(pt[0], pt[1], n, self.letters[i])

    def analyze(self, board, snakes):
        head = self.body[0]
        x = head[0]
        y = head[1]
        limit = self.stepLimit

        next = board.getFourLegalPoints(x, y)
        start = 0
        for pt in next:
            safePaths(self.index, board, pt, start, limit, snakes)

        start = 0
        bestCount = 0
        bestPoint = None
        for pt in next:
            analysis = Analysis()
            analyzePaths(self.index, board, pt, start, limit, analysis)
            if bestCount < analysis.count:
                bestCount = analysis.count
                bestPoint = pt
        if bestPoint:
            self.move = directionFromTo(head,bestPoint)
            self.shout = 'move {} because the best count is {}'.format(self.move, bestCount)
            print(self.shout)

    def chooseMove(self, board):
        if self.move:
            return (self.move, self.shout)
        return ('up','No good here')

    def __str__(self):
        b = str(self.body)
        return 'index:{} move:{} "{}"  body:{}'.format(self.index, self.move, self.shout, b)


def analyzePaths(index, board, fromPt, step, stepLimit, analysis):
    if step >= stepLimit:
        return
    x = fromPt[0]
    y = fromPt[1]
    # Get all the values at this location
    v = board.getAll(x, y)
    if okToVisit(v, index, step):
        letter = v[index]
        if BLOCKED != letter:
            #print('add to count', v, fromPt, analysis)
            analysis.count = analysis.count + 1
            step += 1
            next = board.getFourLegalPoints(x, y)
            for pt in next:
                analyzePaths(index, board, pt, step, stepLimit, analysis)



def safePaths(myIndex, board, fromPt, step, stepLimit, snakes):
    if step >= stepLimit:
        return

    x = fromPt[0]
    y = fromPt[1]
    mysnake = snakes[myIndex].getLength()

    # Get all the values at this location
    v = board.getAll(x, y)

    if not okToVisit(v, myIndex, step):
        return

    letter = v[myIndex]

    others = v.tolist()
    others.pop(myIndex) # remove this snake
    others.pop(0) # remove food in pos 0

    danger = False
    for i, p in enumerate(others):
        if p != EMPTY and p <= letter:
            otherIndex = i + 1
            snake = snakes[otherIndex].getLength()
            if snake >= mysnake:
                """ Another snake the same size as me or larger may also wish to occupy this space. """
                danger = True
                board.set(x, y, myIndex, BLOCKED)
                break
    if not danger:
        step += 1
        next = board.getFourLegalPoints(x, y)
        for pt in next:
            safePaths(myIndex, board, pt, step, stepLimit, snakes)


""" --------------- FLOD ------------------ """

def floodFrom(index, board, fromPt, step, stepLimit):
    if step >= stepLimit:
        return

    x = fromPt[0]
    y = fromPt[1]

    # put a letter into the matrix, at index, to indicate visited at this step
    letter = string.ascii_lowercase[step]

    # Get all the values at this location
    v = board.getAll(x, y)

    # determine status of point
    if okToVisit(v, index, step):

        board.set(x, y, index, letter)

        step += 1
        next = board.getFourLegalPoints(x, y)
        for pt in next:
            floodFrom(index, board, pt, step, stepLimit)

def okToVisit(v, index, step):
    """ Determine if this location can be visited by this flood algorithm """

    # If there is a smaller lower case letter in location then it's been visited by this function
    visited = v[index] in string.ascii_lowercase[:step]
    myBod = v[index] in string.ascii_uppercase

    # next see if this location contains a body part from any other snake
    # convert the remaining into a list removing food (0) and snake that is being processed (index)
    others = v.tolist()
    others.pop(index) # remove this snake
    others.pop(0) # remove food in pos 0
    otherBod = False
    for s in others:
        if s in string.ascii_uppercase:
            otherBod = True
            break

    #print(' v, vis, bd, ot:', v, visited, myBod, otherBod)
    return not visited and not otherBod and not myBod

def directionFromTo(c1, c2):
    assert c1 != c2
    """ c1 is the "from" tile and c2 is the "to" tile """
    c1x = c1[0]
    c1y = c1[1]
    c2x = c2[0]
    c2y = c2[1]
    direction = ''
    if c2x > c1x:
        direction = 'right'
    elif c2x < c1x:
        direction = 'left'
    elif c2y > c1y:
        direction = 'down'
    else:
        direction = 'up'
    return direction

