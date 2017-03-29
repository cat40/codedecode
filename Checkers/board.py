##def condense(startBoard):
##    newBoard = []
##    for row in startBoard
##        row = [x for x in row if x]
#^| only works if middle rows are empty and I finished it


##class piece(object):
##    def __init__(self, x, y, black):
##        self.x = x
##        self.y = y
##        self.black = black #boolean, true if black
##

#validSpaces = [[1,0]*4, [0,1]*4]*4

def contains(l1, l2):
    for x in l2:
        if x in l1:
            return x if x else True #ensures true return
    return False

def condense(startBoard):
    #condenses 8x8 array of spaces into 4x8 array of valid spaces
    evenRows = startBoard[::2] #starts even (with 0)
    oddRows = startBoard[1::2]#takes every other starting on second entry
    newBoard = []
    for odd, even in zip(oddRows, evenRows):
        odd = odd[1::2]
        even = even[::2]
        newBoard.append(even)
        newBoard.append(odd)
    return newBoard

class piece(object):
    def __init__(self, x, y, value):
        #x = [0, 3] place in x direction of CONDENSED array
        self.value = value #numerical value of peices (see below)
        self.x = x
        self.y = x
        self.cords = (x, y)
class move(object):
    #reogrnize this to have a list of normal moves (p, x, y), and a list of killing moves (p, [x...xn], [y...yn], numberKilled)
    def __init__(self, p, end, kill):
        self.start = (p.x, p.y)
        self.end = (x2, y2)
        self.p = p
        
class board(object):
    def __init__(self, boardList):
        pieces = []
        for x, row in enumerate(boardList):
            for y, p in enumerate(row):
                pieces.append(piece(x, y, p)))
        self.peices = pieces
        self.normal1 = [p.cords for p in pieces if p.value == 1]
        self.normal2 = [p.cords for p in pieces if p.value == 2]
        self.normal = [self.normal1, self.normal2]
        self.kings1 = [p.cords for p in pieces if p.value == 10]
        self.kings2 = [p.cords for p in pieces if p.value == 20]
        self.kings = [self.kings1, self.kings2]
        self.player1 = self.normal1+self.kings1
        self.player2 = self.normal2+self.kings2
        self.empty = [p.cords for p in pieces if p.value == 0]
        #might not need these, but can kind of tell who's winning
        self.points1 = len(self.normal1) + len(self.kings1)*2 #assuming kings 2* as valuble as normal pieces
        self.points2 = len(self.normal2) + len(self.kings2)*2
        self.winning = 2 if self.points2 > self.points1 else 1 if self.points1 > self.points2 else 0

    def getMoves(self, player):
        #checks if either space is clear
        #direciton is 1 if towards player 2, and -1 if towards player 1
        def checkClear(clear, p, direction):
            x = p.x
            y = p.y + direction
            for i in ((x+1, y), (x-1, y)):
                if i in clear: yield i
                    
        #after a peice is known to be able to jump, check how many times it can jump, and go with that move.
        #Unless we want to make it spectatcularly awful, in which case don't do that
        def checkKill(enemy, p, direction):
            x = p.x
            y = p.y+direction+direction
            for i in ((x+2, y), (x-2, y)):
                if i in clear:
                    newP = piece(p.x, p.y + direction*2, p.value)
                    if checkClear(clear, newP, direction):
        #might reorganize to return tuple of normal and king moves, but for now is generator and switches silently (could also just switch noise). see move class
        #normal moves (no jumping):
        for p in self.normal[player-1]:
            
    
'''
def my_ai(boasrd)
return move (peice, target)

board is 2d array of ints
empty is 0, play 1 is 1, player 2 is 2
10/20 are kings
8x8
-> can condense to 4x4

make hiliariously bad, cuaseI cant make it good
return cords of peice location, and target
must be valid move

reccomended course:
    find list of all possible peices and move
    only every other square is usable
    Will have to string together jumping moves somehow


empty:
0 = empty space
player 1:
1 = peice
10 = king
player 2:
2 = peice
20 = king
'''
