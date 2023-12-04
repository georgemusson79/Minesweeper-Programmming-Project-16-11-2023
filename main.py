#main.py
import pygame
import time
from GameSetup import GameSetup
from MainGame import MainGame
from gameState import GameStates
import gameState
from label import Label
from MainMenu import MainMenu
import sys


global WINDOW_WIDTH
WINDOW_WIDTH=800
global WINDOW_HEIGHT
WINDOW_HEIGHT=800




def main():
    sys.setrecursionlimit(99*99) #increase recursion limit to handle the largest possible board
    pygame.init()
    running=True
    surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.SCALED,vsync=1)
    gameState.setGameState(GameStates.MAIN_MENU)
    print(pygame.get_error())
    mainMenu=MainMenu(surface)
    mainGame=MainGame(surface)
    gameSetup=GameSetup(surface)
    
    while running:

        
        #main game loop
        surface.fill((0,0,0)) #clear the screen
        gState=gameState.getGameState()
        match gState:
            case GameStates.MAIN_MENU:
                mainMenu.update()
            case GameStates.MAIN_GAME:
                mainGame.update()
            case GameStates.GAME_SETUP:
                gameSetup.update()
                if gameSetup.submitPressed:
                    #if the user has pressed the submit button in gameSetup, check if conditions are correct and if so update game state
                    gameSetup.submitPressed=False
                    try:
                        margin=WINDOW_WIDTH/10 #distance between the edges of the board on the x axis and edge of the screen
                        boardX=margin
                        boardWidth=WINDOW_WIDTH-(2*margin)
                        mainGame.generateBoard(gameSetup.boardWidth,gameSetup.boardHeight,gameSetup.mineCount,pygame.Rect(boardX,0,boardWidth,boardWidth)) #board is a square
                        time.sleep(1)
                        gameState.setGameState(GameStates.MAIN_GAME)
                    except Exception as e:
                        print(e)


   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.update()


if __name__=="__main__":
    main()