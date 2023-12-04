#mainmenu.py
from button import Button
import pygame
import random
from gameState import GameStates
import gameState
class MainMenu:
    active=False
    buttons=[]
    surface:pygame.Surface
    bg:pygame.Surface
    title:pygame.Surface

    #dimensions for rendering the title to the screen
    titleX:int
    titleY:int
    titleW:int
    titleH:int



    def __init__(self,surface:pygame.Surface):
        #initialises variables, loads background and scales to fit window,loads buttons into buttons array
        self.surface=surface
        self.bg=pygame.image.load("assets//img//MainMenu_bg.png")
        self.title=pygame.image.load("assets//img//title.png")

        #set title width to be width of window, title height to be 1/4 the height of the window
        self.titleH=surface.get_height()/4
        self.titleW=surface.get_width()
        self.titleX=0
        self.titleY=0-self.titleH # load title above the screen
        self.title=pygame.transform.scale(self.title,(self.titleW,self.titleH)) # scale title to fit dimensions
        self.bg=pygame.transform.scale(self.bg,(self.surface.get_width(),self.surface.get_height()))
        print(pygame.get_error())
        #main menu constructor, take Surface object as argument for rendering to screen
        #set button dimensions for start button
        buttonWidth=self.surface.get_width()/3
        buttonHeight=self.surface.get_height()/8
        buttonX=self.surface.get_width()/2-(buttonWidth/2)
        buttonY=self.surface.get_height()*3/8
        self.buttons=[Button(surface,buttonX,buttonY,buttonWidth,buttonHeight,"assets//img//button1.png",gameState.setGameState,lcArgs=GameStates.GAME_SETUP)]
    def render(self):
        #renders the MainMenu to the screen returns nothing
        self.surface.blit(self.bg,(0,0)) #render background to window
        self.surface.blit(self.title,(self.titleX,self.titleY)) #render title to window
        for button in self.buttons:
            button.render()
   

    def update(self):
        #called every frame if MainMenu is active
        if self.titleY<0:
            self.titleY+=self.titleH/60 #while title is off screen keep moving it into frame
        self.render()
   
        for button in self.buttons:
            button.handleClick()
