import pgzrun

# this is defining the game window's height and width, and the tile's size
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

#define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W   KG      W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W       P      W",
       "W  WWWWWWWWWW  W",
       "W       GK     W",
       "W              W",
       "W              W",
       "WWWWWWWWWWWWWWWW"]

# Convert grid (x, y) to screen pixel coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# Draw floor tiles
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))
# Setup player
def SetupGame():
    global player
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            row = MAP[y].ljust(GRID_WIDTH)  # pad in case row is short
            if row[x].upper() == "P":
                player.pos = GetScreenCoords(x, y)
# Draw walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            row = MAP[y].ljust(GRID_WIDTH)
            square = row[x]
            pos = GetScreenCoords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D":
                screen.blit("door", pos)
            # You can add more tile types like "K", "G" here later
# Main draw loop
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    player.draw()
# Setup and run
SetupGame()
pgzrun.go()
