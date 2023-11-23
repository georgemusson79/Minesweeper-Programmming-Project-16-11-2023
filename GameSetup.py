import pygame
from button import Button
from TextField import TextField
class GameSetup:
    surface=None
    textFieldList=[]
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
        self.textFieldList=[TextField(surface,buttonX,buttonY,buttonWidth,buttonHeight,8,(255,255,255))]
        
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
    def submit(self):
        pass

