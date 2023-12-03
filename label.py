import pygame
class Label:
    surface:pygame.Surface
    x:int
    y:int
    w:int
    h:int
    text:str
    lineCharLimit:int #number of characters per line, unlimited if set to -1
    color:pygame.Color
    font=pygame.font.Font
    textImgs=[]
    textChunks=[]
    active:bool
    def __init__(self,surface:pygame.surface,x:int,y:int,w:int,h:int,text:str="",color=(255,255,255),lineCharLimit=-1,font:pygame.font.Font=None):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        self.lineCharLimit=lineCharLimit
        if (font==None): #if font is None set to default font
            self.font=pygame.font.SysFont(None,100)
        else:
            self.font=font
        self.surface=surface
        self.setText(text,color)
    def render(self):
        #renders text to surface
        lineNumber=0
        longestString=max(self.textChunks,key=len) #get biggest string on a single line
        charWidth=self.w/len(longestString) #width of each character will be the width of the textbox divided by the number of chars in the biggest string
        charHeight=self.h/len(self.textImgs)

        wordIndex=0 #position of img as text in text chunks
        for img in self.textImgs:
            img=pygame.transform.scale(img,(len(self.textChunks[wordIndex])*charWidth,charHeight)) #scale text to be text box height divided by number of lines, width is character width*num of chars in word
            pos=(self.x,self.y+(charHeight*lineNumber)) #place text based on line number
            self.surface.blit(img,pos) 
            lineNumber+=1
            wordIndex+=1


    def setText(self,text:str,color:pygame.Color=(255,255,255)):
        #split text based on lineCharLimit and create a surface for each line
        self.textImgs=[]
        self.text=text
        if self.lineCharLimit==-1:
            self.textChunks=[text]
        else:
            self.textChunks=[text[i:i+self.lineCharLimit] for i in range(0,len(text),self.lineCharLimit)]
        self.color=color
        for t in self.textChunks:
            fontImg=self.font.render(t,True,self.color)
            self.textImgs.append(fontImg)
        

        