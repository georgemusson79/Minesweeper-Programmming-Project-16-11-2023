import pygame
from button import Button
from TextField import TextField
from label import Label
from enum import IntEnum
import string

class GameAttrs(IntEnum):
    #int enums to improve readability
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
    submitPressed=False


    def __init__(self,surface:pygame.Surface):
        self.surface=surface

        #set button position relative to the size of the window
        buttonWidth=self.surface.get_width()/3
        buttonHeight=self.surface.get_height()/8
        buttonX=self.surface.get_width()/2-(buttonWidth/2)
        buttonY=self.surface.get_height()*6/8
        self.buttons=[Button(self.surface,buttonX,buttonY,buttonWidth,buttonHeight,"assets/img/submitButton.png",self.submit)] #submit button
        self.bg=pygame.image.load("assets//img//GameSetup.png")
        self.bg=pygame.transform.scale(self.bg,(self.surface.get_width(),self.surface.get_height()))
        textFieldWidth=self.surface.get_width()/2
        startY=self.surface.get_height()/4 #starting y pos for first text field
        startX=(self.surface.get_width()/2)-(textFieldWidth/2) #starting x pos for first text field
        textFieldHeight=surface.get_height()/20
        gap=self.surface.get_height()/5 #y distance between 2 textboxes
        allowedChars="0123456789" #only numbers may be inputted into the text fields
        self.textFieldList=[TextField(surface,startX,startY,textFieldWidth,textFieldHeight,2,(255,255,255),allowedCharacters=allowedChars),TextField(surface,startX,startY+gap,textFieldWidth,textFieldHeight,2,(255,255,255),allowedCharacters=allowedChars),TextField(surface,startX,startY+(gap*2),textFieldWidth,textFieldHeight,4,(255,255,255),allowedCharacters=allowedChars)]
        labelHeight=textFieldHeight
        labelCharWidth=surface.get_width()/40
        self.labelsList=[Label(surface,self.textFieldList[GameAttrs.BOARD_WIDTH].x,self.textFieldList[GameAttrs.BOARD_WIDTH].y-labelHeight,labelCharWidth*len("Board Width:"),labelHeight,"Board Width:"),Label(surface,self.textFieldList[GameAttrs.BOARD_WIDTH].x,self.textFieldList[GameAttrs.BOARD_HEIGHT].y-labelHeight,labelCharWidth*len("Board Height:"),labelHeight,"Board Height:"),Label(surface,self.textFieldList[GameAttrs.BOARD_WIDTH].x,self.textFieldList[GameAttrs.MINE_COUNT].y-labelHeight,labelCharWidth*len("Mine Count:"),labelHeight,"Mine Count:")]
    def render(self):
        self.surface.blit(self.bg,(0,0))
        for button in self.buttons:
            button.render()
        for textField in self.textFieldList:
            textField.render()
        for label in self.labelsList:
            label.render()
            
    def update(self):
        #renders menu to screen and handles button clicks and user input to text fields
        self.render()
        for button in self.buttons:
            button.handleClick()
        for textField in self.textFieldList:
            textField.checkIfClicked()
            textField.handleInput()

    def submit(self):
        #updates attributes and sets submitPressed to true for the main loop to verify everything is correct and handle game state switching
        for textField in self.textFieldList:
            if textField.text=="":
                print("All fields must contain a value")
                return 0
        self.boardHeight=int(self.textFieldList[GameAttrs.BOARD_HEIGHT].text)
        self.boardWidth=int(self.textFieldList[GameAttrs.BOARD_WIDTH].text)
        self.mineCount=int(self.textFieldList[GameAttrs.MINE_COUNT].text)
        self.submitPressed=True
  

