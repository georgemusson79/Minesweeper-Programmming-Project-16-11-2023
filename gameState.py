from enum import Enum
class GameStates(Enum):
    MAIN_MENU=1
    MAIN_GAME=2
    GAME_SETUP=3
    LOAD_FILE=4
global gameState
gameState=None

def setGameState(state:GameStates):
    #used to indicate which part of the code is running, holds a value from the GameStates enum
    global gameState
    gameState=state

def getGameState():
    #used to indicate which part of the code is running, holds a value from the GameStates enum
    global gameState
    return gameState