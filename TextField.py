import pygame
import pygame.font
import string
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
    def __init__(self,surface:pygame.Surface,x: int,y:int ,w:int,h:int,maxLength:int,color:pygame.Color=pygame.Color(255,255,255),textColor:pygame.Color=pygame.Color(0,0,0),allowedCharacters:str=string.printable,text=""):
        self.surface=surface
        self.x=x
        self.text=""
        self.y=y
        self.w=w
        self.h=h
        self.font=pygame.font.Font(None,48)
        self.allowedCharacters=allowedCharacters
        self.color=color
        self.textColor=textColor
        self.maxLength=maxLength

    def render(self):
        r=pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.surface,self.color,r) #draw background to screen
        imgText=self.font.render(self.text,True,self.textColor) #load text as image
        charWidth=self.w/self.maxLength #get pixel width of each character by dividing width of the textbox by max characters allowed
        imgTextWidth=charWidth*len(self.text) #get text pixel with by multiplying charWidth by size of string
        imgText=pygame.transform.scale(imgText,(imgTextWidth,self.h)) #height will be the same size as textbox height
        self.surface.blit(imgText,(r.x,r.y))
    def handleInput(self):
        keys=pygame.key.get_pressed()
        for key,state in enumerate(keys):
            if state:
                if key==pygame.K_BACKSPACE:
                    if len(self.text)>0:
                        self.text=self.text[:-1]
                elif key in self.allowedCharacters and len(self.text)<self.maxLength:
                    self.text+=pygame.key.name(key)

                

                
                