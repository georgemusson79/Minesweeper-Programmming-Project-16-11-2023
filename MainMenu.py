#mainmenu.py
from button import Button
import pygame
import random
from gameState import GameStates
import gameState
class MainMenu:
    active=False
    buttons=[]
    surface=None
    bg=None



    def __init__(self,surface):
        #initialises variables, loads background and scales to fit window,loads buttons into buttons array
        self.surface=surface
        self.bg=pygame.image.load("assets//img//MainMenu_bg.jpg")
        self.bg=pygame.transform.scale(self.bg,(self.surface.get_width(),surface.get_height()))
        print(pygame.get_error())
        #main menu constructor, take Surface object as argument for rendering to screen
        self.buttons=[Button(surface,100,100,300,100,"assets//img//button1.png",gameState.setGameState,lcArgs=GameStates.MAIN_GAME)]
    def render(self):
        #renders the MainMenu to the screen returns nothing
        self.surface.blit(self.bg,(0,0))
        for button in self.buttons:
            button.render()
        pass

    def update(self):
        #called every frame if MainMenu is active
        self.render()
   
        for button in self.buttons:
            button.handleClick()
