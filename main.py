#main.py
import pygame
from MainGame import MainGame
from gameState import GameStates
import gameState
from MainMenu import MainMenu


global WINDOW_WIDTH
WINDOW_WIDTH=600
global WINDOW_HEIGHT
WINDOW_HEIGHT=600




def main():
    pygame.init()
    running=True
    surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),pygame.SCALED,vsync=1)
    gameState.setGameState(GameStates.MAIN_MENU)
    print(pygame.get_error())
    mainMenu=MainMenu(surface)
    mainGame=MainGame(surface)
    mainGame.generateBoard(15,15,40,pygame.Rect(0,0,500,500))
    
    while running:
        surface.fill((0,0,0)) #clear the screen
        gState=gameState.getGameState()
        match gState:
            case GameStates.MAIN_MENU:
                mainMenu.update()
            case GameStates.MAIN_GAME:
                mainGame.update()

   
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.update()


if __name__=="__main__":
    main()