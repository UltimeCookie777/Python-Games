import os


emptyCell = "-"
redCell = "R"
yellowCell = "Y"
playerRound = "Red"

# y = 6, x = 7
table = [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
]

# Check if the cell below is empty
def checkBelow(x: int, y: int) -> bool:
    if y == 5:
        return False

    return table[x][y + 1] == emptyCell


# Check if the column is full
def checkColumn(x: int) -> bool:
    return emptyCell in table[x]

# Prints out the current board.
def printTable() -> None:
    out = ""

    for y in range(0, 6):
        for x in range(0, 7):
            out += table[x][y] + " "
        out += "\n"
    print("\n" + out)


# Asking where to play
def asking() -> int:
    x = 0
    while True:
        try:
            x = int(input("\nChoose a column (1-7) : "))
        except:
            print(
                "Please only enter a number. If you want to stop the program, use the number 69."
            )
            continue

        # Added this to avoid endless loop
        if x == 69:
            raise Exception("STOP PROGRAM")

        if not (x in [c for c in range(1, 8)]):
            print("Enter a number between 1 and 7.")
        else:
            if checkColumn(x - 1):
                x -= 1
                break
            else:
                print("This column is full.")
    return x


# Add a 'color' piece in the x column
def addPiece(color: str, x: int) -> int:
    y = 0
    while checkBelow(x, y):
        y += 1

    table[x][y] = color
    return y


# Returns the current player color
def getColor() -> str:
    return redCell if playerRound == "Red" else yellowCell


# Change the current player
def changePlayer(playerRound: str) -> str:
    if playerRound == "Red":
        playerRound = "Yellow"
    else:
        playerRound = "Red"

    return playerRound


# Check for win based on the last posed piece
def checkWin(x: int, y: int) -> bool:
    # Check horizontal win
    sum = 0
    for x_ in range(0, 7):
        if table[x_][y] == getColor():
            sum += 1
            if sum >= 4:
                return True
        else:
            sum = 0

    # Check vertical win
    sum = 0
    for y_ in range(0, 6):
        if table[x][y_] == getColor():
            sum += 1
            if sum >= 4:
                return True
        else:
            sum = 0

    # Check top left to bottom right diagonal win
    for y1 in range(0, 3):
        for x1 in range(0, 4):
            sum = 0
            for z1 in range(0, 4):
                if table[x1 + z1][y1 + z1] == getColor():
                    sum += 1
                if sum == 4:
                    return True

    # Check top right to bottom left diagonal win
    for y2 in range(0, 3):
        for x2 in range(3, 7):
            sum = 0
            for z2 in range(0, 4):
                if table[x2 - z2][y2 + z2] == getColor():
                    sum += 1
                if sum == 4:
                    return True

    return False


# Start of the game
os.system("cls")
print("========== Power 4 ==========")
print(f"\n{playerRound} Player starts.\n")

x = asking()
y = addPiece(redCell, x)

# Running game
while not (checkWin(x, y)):
    playerRound = changePlayer(playerRound)

    os.system("cls")
    print("========== Power 4 ==========")
    print(f"\n{playerRound} Player plays.\n")
    printTable()

    x = asking()
    y = addPiece(getColor(), x)

os.system("cls")

print("========== Power 4 ==========")
print(f"\n{playerRound} Player won the game!\n")
printTable()
