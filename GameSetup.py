import pygame
from button import Button
from TextField import TextField
from label import Label
from enum import IntEnum

class GameAttrs(IntEnum):
    BOARD_WIDTH=0
    BOARD_HEIGHT=1
    MINE_COUNT=2


class GameSetup:
    surface:pygame.Surface=None
    textFieldList=[]
    labelsList=[]
    buttons=[]
    boardWidth=0
    boardHeight=0
    mineCount=0
    def __init__(self,surface:pygame.Surface):
        self.surface=surface

        #set button position relative to the size of the window
        buttonWidth=self.surface.get_width()/3
        buttonHeight=self.surface.get_height()/8
        buttonX=self.surface.get_width()/2-(buttonWidth/2)
        buttonY=self.surface.get_height()*6/8
        self.buttons=[Button(self.surface,buttonX,buttonY,buttonWidth,buttonHeight,"assets/img/submitButton.png",self.submit)]
        self.bg=pygame.image.load("assets//img//GameSetup.png")
        self.bg=pygame.transform.scale(self.bg,(self.surface.get_width(),self.surface.get_height()))
        textFieldWidth=self.surface.get_width()/2
        startY=self.surface.get_height()/3 #starting y pos for first text field
        startX=(self.surface.get_width()/2)-(textFieldWidth/2) #starting x pos for first text field
        textFieldHeight=surface.get_height()/20
        self.textFieldList=[TextField(surface,startX,startY,textFieldWidth,textFieldHeight,999,(255,255,255))]
        labelHeight=textFieldHeight
        labelCharWidth=surface.get_width()/40
        self.labelsList=[Label(surface,self.textFieldList[GameAttrs.BOARD_WIDTH].x,self.textFieldList[GameAttrs.BOARD_WIDTH].x-labelHeight,labelCharWidth*len("Board Width:"),labelHeight,"Board Width:")]
        
    def render(self):
        self.surface.blit(self.bg,(0,0))
        for button in self.buttons:
            button.render()
        for textField in self.textFieldList:
            textField.render()
            
    def update(self):
        self.render()
        for button in self.buttons:
            button.handleClick()
        for textField in self.textFieldList:
            textField.checkIfClicked()
            textField.handleInput()
        for label in self.labelsList:
            label.render()
    def submit(self):
        pass

