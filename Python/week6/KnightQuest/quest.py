########## 1.3 ##########
import pgzrun 

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.25

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
#########################

########## 1.5 ##########
MAP = ["WWWWWWWWWWWWWWWW",
       "W           K  W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W  K           D",
       "WWWWWWWWWWWWWWWW"]
#########################

########## 1.4 ##########
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))
#########################

########## 2.1 ##########
def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
#########################

########## 1.7, 3.0, 3.3 ##########
def SetupGame():
    global player, keysToCollect, gameOver, guards
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)
#########################

########## 1.6 ##########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
#########################

########## 1.8, 3.1 ##########
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
#########################

############# 3.5 ##############
def drawGameOver():
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    screen.draw.text("GAME OVER", midbottom=screenMiddle,
                     fontsize=GRID_SIZE, color="indigo", owidth=1)
#########################

############# 4.1 ##################
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -= 1

    guard.pos = GetScreenCoords(guardX, guardY)

    if guardX == playerX and guardY == playerY:
        gameOver = True
#########################

########## 4.2 ##########
def MoveAllGuards():
    for guard in guards:
        MoveGuard(guard)
#########################

########## draw() ##########
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        drawGameOver()
#########################

########## 2.2, 3.2 ##########
def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]

    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            gameOver = True

    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break

    player.pos = GetScreenCoords(x, y)
#########################

########## 2.3 ##########
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.DOWN:
        MovePlayer(0, 1)
#########################

# Start the game
SetupGame()
clock.schedule_interval(MoveAllGuards, GUARDMOVEINTERVAL)
pgzrun.go()
