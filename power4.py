import os


emptyCell = "-"
redCell = "R"
yellowCell = "Y"
playerRound = "Red"

# y = 6, x = 7
table = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
#table = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]

# Check if the cell below is empty
def checkBelow(x,y):
    if y==5:
        return False

    return table[x][y+1] == emptyCell

# Check if the column is full
def checkColumn(x):
    return table[x][0] == emptyCell

def printTable():
    
    out = ""
    
    for y in range(0,6):
        for x in range(0,7):
            out += table[x][y] + " "
        out += "\n"
    print("\n" + out)

# Asking where to play
def asking():
    x=0
    while True:
        
        try:
            x = int(input("\nChoose a column (1-7) : "))
        except:
            print("Please only enter a number. If you want to stop the program, use the number 69.")
            continue
        
        # Added this to avoid endless loop
        if x == 69:
            raise Exception('STOP PROGRAM')
        
        if not(x in [c for c in range(1,8)]):
            print("Enter a number between 1 and 7.")
        else:
            if not(checkColumn(x)):
                print('This column is full.')
                continue
            
            x-=1
            break
    return x
# Add a 'color' piece in the x column
def addPiece(color, x):
    
    y = 0
    while checkBelow(x,y):
        y+=1

    table[x][y] = color
    return y

# Returns the current player color
def getColor():
    return redCell if playerRound == "Red" else yellowCell

# Change the current player
def changePlayer(playerRound):
    if playerRound == "Red":
        playerRound = "Yellow"
    else:
        playerRound = "Red"

    return playerRound
# Check for win based on the last posed piece
def checkWin(x,y):
    return

# Start of the game
os.system("cls")
print("========== Power 4 ==========")
print(f"\n{playerRound} Player starts.\n")

x = asking()
y = addPiece(redCell, x)

# Running game
while not(checkWin(x,y)):
    
    os.system("cls")
    print("========== Power 4 ==========")
    print(f"\n{playerRound} Player plays.\n")
    printTable()
    
    playerRound = changePlayer(playerRound)
    x = asking()
    y = addPiece(getColor(), x)
    