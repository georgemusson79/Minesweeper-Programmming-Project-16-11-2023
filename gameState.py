from enum import Enum
class GameStates(Enum):
    #used to indicate what part of the game is running
    MAIN_MENU=1
    MAIN_GAME=2
    GAME_SETUP=3
    LOAD_FILE=4
global gameState
gameState=None #private, should use get and set methods to acess

def setGameState(state:GameStates):
    global gameState
    gameState=state

def getGameState():
    global gameState
    return gameState