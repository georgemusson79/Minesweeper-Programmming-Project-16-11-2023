from re import L
import pygame
class Label:
    surface:pygame.Surface
    x:int
    y:int
    w:int
    h:int
    text:str
    color:pygame.Color
    font=pygame.font.Font
    fontImg: pygame.Surface
    active:bool
    def __init__(self,surface:pygame.surface,x:int,y:int,w:int,h:int,text:str="",color=(255,255,255),font:pygame.font.Font=None):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        if (font==None): #if font is None set to default font
            self.font=pygame.font.SysFont(None,100)
        else:
            self.font=font
        self.surface=surface
        self.setText(text,color)
    def render(self):
        #renders text to surface
        self.fontImg=pygame.transform.scale(self.fontImg,(self.w,self.h))
        self.surface.blit(self.fontImg,(self.x,self.y))


    def setText(self,text:str,color:pygame.Color=(255,255,255)):
        #set text and update textImg
        self.text=text
        self.color=color
        self.fontImg=self.font.render(self.text,True,self.color)

        

        