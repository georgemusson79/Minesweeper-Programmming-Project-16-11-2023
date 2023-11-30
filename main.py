#main.py
import pygame
from GameSetup import GameSetup
from MainGame import MainGame
from gameState import GameStates
import gameState
from MainMenu import MainMenu


global WINDOW_WIDTH
WINDOW_WIDTH=1200
global WINDOW_HEIGHT
WINDOW_HEIGHT=900




def main():
    pygame.init()
    running=True
    surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.SCALED,vsync=1)
    gameState.setGameState(GameStates.MAIN_MENU)
    print(pygame.get_error())
    mainMenu=MainMenu(surface)
    mainGame=MainGame(surface)
    gameSetup=GameSetup(surface)
    
    while running:
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
                        mainGame.generateBoard(gameSetup.boardWidth,gameSetup.boardHeight,gameSetup.mineCount,pygame.Rect(0,0,900,900))
                        gameState.setGameState(GameStates.MAIN_GAME)
                    except Exception as e:
                        print(e)


   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.update()


if __name__=="__main__":
    main()