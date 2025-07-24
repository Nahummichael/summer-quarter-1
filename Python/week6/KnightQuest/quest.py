import pgzrun

# this is defining the game window's height (12 tiles tall) and width(16 tiles wide), and the tile's size
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
       "W      P       D",
       "W  WWWWWWWWWW  W",
       "W       GK  W  W",
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

############# 2.1 ##############

# this function takes in an actor as an argument &
# returns the position of the actor on the grid
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
###################################
# Setup player
############ 1.7 ###############
def SetupGame():
    global player
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]  # pad in case row is short
            if square == "P":
                player.pos = GetScreenCoords(x, y)
# Draw walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            pos = GetScreenCoords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D":
                screen.blit("door", pos)
            # You can add more tile types like "K", "G" here later
# Main draw loop

def drawActors():
    player.draw()

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    drawActors()

########### 2.2 ###########
def MovePlayer(dx, dy):
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP [y][x]
    if square == "W":
        return
    elif square == "D":
        return
    player.pos = GetScreenCoords(x,y)
#####################################

########### 2.3 ##############
# this function gets a key from the user and moves the player based on the input
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1,0) # Player moves left one on the grid
    elif key == keys.UP:
        MovePlayer(0,-1)# Player moves up one on the grid
    elif key == keys.RIGHT:
        MovePlayer(1,0) # Player moves right one on the grid
    elif key == keys.DOWN:
        MovePlayer(0,1) # Player moves down one on the grid

# Setup and run
SetupGame()
pgzrun.go()
