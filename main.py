emptyCell = "-"
redCell = "R"
yellowCell = "Y"


# y = 6, x = 7
tableau = [[emptyCell] * 7] * 6
print(tableau)


# Check if the cell below is empty
def checkBelow(x,y):
    if y==5:
        return False

    return tableau[x][y+1] == emptyCell

# Check if the column is full
def checkColumn(x):
    return tableau[x][0] == emptyCell

# Add a 'color' piece in the x column
def addPiece(color, x):
    
    y = 0
    while checkBelow(x,y):
        y+=1

    tableau[x][y] == color

# Check for win based on the last posed piece
def checkWin(x,y):
    return