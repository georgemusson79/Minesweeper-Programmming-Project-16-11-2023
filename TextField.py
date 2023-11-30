import pygame
import pygame.font
import string
import time
class TextField:
    x: int
    y: int
    w: int
    h: int
    surface: pygame.Surface
    font:pygame.font.Font
    text: str
    color:pygame.Color
    textColor:pygame.Color
    maxLength: int
    allowedCharacters: str
    timeSinceLastPressed=0
    isFocused=False
    active=True
    def __init__(self,surface:pygame.Surface,x: int,y:int ,w:int,h:int,maxLength:int,color:pygame.Color=pygame.Color(255,255,255),textColor:pygame.Color=pygame.Color(0,0,0),allowedCharacters:str=string.printable,text=""):
        self.surface=surface
        self.x=x
        self.text=""
        self.y=y
        self.w=w
        self.h=h
        self.font=pygame.font.Font(None,100)
        self.allowedCharacters=allowedCharacters
        self.color=color
        self.textColor=textColor
        self.maxLength=maxLength


    def isColliding(self,x:int,y:int):
        #takes x and y coordinate for input, check if position collides with textField, returns true if so, otherwise returns false
        if (x>=self.x and x<self.x+self.w) and (y>=self.y and y<self.y+self.h):
            return True
        return False
    def checkIfClicked(self):
        #checks if the user has clicked on the text box, if so set isFocused to true otherwise set to false
        if not self.active:
            return
        x,y=pygame.mouse.get_pos()
        btn=pygame.mouse.get_pressed()
        if btn[0]:
            if self.isColliding(x,y) and self.active:
                self.isFocused=True
            else:
                self.isFocused=False

    def render(self):
        r=pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.surface,self.color,r) #draw background to screen
        imgText=self.font.render(self.text,True,self.textColor) #load text as image
        if len(self.text)<8:
            charWidth=self.w/8 #if there are less than 8 characters one character takes up an 8th of the textbox
        else:
           charWidth=self.w/len(self.text) #get pixel width of each character by dividing width of the textbox by max characters allowed
        imgTextWidth=charWidth*len(self.text) #get text pixel with by multiplying charWidth by size of string
        imgText=pygame.transform.scale(imgText,(imgTextWidth,self.h)) #height will be the same size as textbox height
        self.surface.blit(imgText,(r.x,r.y)) #top left corner of text is in top left corner of text box
    def handleInput(self):
        #checks if user has typed anything if the textbox is focused and active and enter it into the text field otherwise return nothing
        if not self.active or not self.isFocused:
            return
        keys=pygame.key.get_pressed()
        if time.time()-self.timeSinceLastPressed<0.1: #checks if time since a key was last pressed is greater than 100ms otherwise returns without checking key presses
            return
        for key in range(0,255):
            if keys[key]:
                self.timeSinceLastPressed=time.time() #if key is pressed update
                if key==pygame.K_BACKSPACE:
                    if len(self.text)>0:
                        self.text=self.text[:-1]
                elif pygame.key.name(key) in self.allowedCharacters and len(self.text)<self.maxLength:
                    self.text+=pygame.key.name(key)

                

                
                