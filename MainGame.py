import pygame
import random
import math
from Tile import Tile
from BoardException import BoardException
class MainGame:
    board=None
    boardGenerated=False
    flagTexture=None
    mineCount=0
    boardW=0 #represents number of tiles on the board on the x axis
    boardH=0 #represents number of tiles on the board on the y axis
    boardDims=pygame.Rect(0,0,0,0)
    surface=None
    clickCoolDownMaxTime=10 #variables to allow for clicking only after 10 frames have passed since last click
    clickCoolDownTimePassed=0
    font=None #font for rendering numbers to screen
    openCount=0
    gameOver=False

    def openTile(self,x,y):
        #sets tile at x,y position to isOpen if it exists
        #if the surroundingMineCount is 0 on the tile it'll also recursively call openTile() on the surrounding tiles until it finds a tile with a surroundingMineCount greater than 0
        if self.isOnBoard(x,y) and not self.board[x][y].isOpen and not self.board[x][y].isFlagged:
            self.board[x][y].isOpen=True
            self.board[x][y].surroundingMineCount=self.getMineCountAroundPt(x,y)
            if (self.board[x][y].surroundingMineCount==0):
                for posX in range(x-1,x+2):
                    for posY in range(y-1,y+2):
                       
                        if (x,y)!=(posX,posY) and self.isOnBoard(posX,posY) and not self.board[posX][posY].isMine:
                            self.openTile(posX,posY)
                            
             

    def __init__(self,surface):
        self.surface=surface
        self.font=pygame.font.Font(None,64)

    def scatterMines(self):
        #places mines randomly around the board where isOpen=false, returns void
        #this is called after the first tile is opened to prevent the player from landing on a mine immediately
        count=self.mineCount
        while count>0:
            x=random.randint(0,self.boardW-1)
            y=random.randint(0,self.boardH-1)
            if not self.board[x][y].isMine and not self.board[x][y].isOpen:
                self.board[x][y].isMine=True
  
                count-=1


    def boardHandleClicks(self):
        #allows the user to interact with the board with left and right clicks
        #left clicks for opening tiles, right clicks for flagging tiles
        #uses boardDims for getting the cursor position relative to the board
        #tiles that are flagged cannot be opened, however they can be unflagged by right clicking again
        #returns void
        x,y=pygame.mouse.get_pos()
        btn=pygame.mouse.get_pressed()
        tileWidth=int(self.boardDims.w/self.boardW) #get width and height of each individual tile in pixels
        tileHeight=int(self.boardDims.h/self.boardH)

        #boardX and boardY represent the tile that the mouse is currently hovering over starting from 0
        #e.g. the tile on the first row and first column would be 0 0, the tile on the first row, second column would be 1 0 etc
        boardX=int((x-self.boardDims.x)/tileWidth)
        boardY=int((y-self.boardDims.y)/tileHeight)
        
        if self.isOnBoard(boardX,boardY) and self.clickCoolDownTimePassed>self.clickCoolDownMaxTime:
            if btn[0]: #if leftclick and no flag has been placed
                if self.openCount==0:
                    #if this is the users first left click scatter mines on all tiles except selected one
                    #afterwards continue normally
                    self.board[boardX][boardY].isOpen=True
                    self.scatterMines()
                    self.board[boardX][boardY].isOpen=False
                self.openTile(boardX,boardY)   
                self.clickCoolDownTimePassed=0
                self.openCount+=1
             
            elif btn[2] and not self.board[boardX][boardY].isOpen: #if right click and tile not opened
                self.board[boardX][boardY].isFlagged= not self.board[boardX][boardY].isFlagged #if flagged becomes not flagged and vice versa
                self.clickCoolDownTimePassed=0
        self.clickCoolDownTimePassed+=1
       
        

    def isOnBoard(self,x,y):
        #checks if a position is on the board, if so returns true, otherwise returns false
        if x>=0 and x<self.boardW and y>=0 and y<self.boardH:
            return True
        return False

    def setBoardDims(self,x,y,w,h):
        #used to set the board position for rendering to the screen
        #takes x and y values and width and height values, all ints
        #these represent the amount of pixels the board will take up on the screen
        #also updates the flag texture to fill entire square
        #returns void
        if w<1 or h<1:
            raise BoardException("board dimension width and height must be greater than 0")
        self.boardDims=pygame.Rect(x,y,w,h)
        self.flagTexture=pygame.image.load("assets\\img\\flag.png")
        self.flagTexture=pygame.transform.scale(self.flagTexture,(w/self.boardW,h/self.boardH))

    def generateBoard(self,width,height,mineCount,renderDims):
        #generates board that will be played on, parameters are board width, height and number of mines, all ints, returns void
        #also takes a pygame.Rect resembling the rendering dimensions of the board on the screen in pixels
        #exceptions to be raised in case board parameters are invalid
        if (width*height)<=mineCount:
            raise BoardException("mineCount must be less than width*height")
        if width<1 or height<1:
            raise BoardException("width and height must be greater than 0")
        if mineCount<1:
            raise BoardException("mineCount must be at least 1")
        if type(renderDims)!=pygame.Rect:
            raise BoardException("renderDims not of type pygame.Rect")

    
        self.boardW=width
        self.boardH=height
        self.mineCount=mineCount
        self.setBoardDims(renderDims.x,renderDims.y,renderDims.w,renderDims.h)
        self.board=[[Tile() for y in range(height)]for x in range(width)]
        self.boardGenerated=True

    def update(self):
        #to be called every frame while gameState equals MAIN_GAME
        if not self.boardGenerated:
            return
        self.renderBoard()
        self.boardHandleClicks()

   

    def getMineCountAroundPt(self,posX,posY):
        #returns number of tiles around a point whose isMine is set to True
        #does not include the point itself if it is a mine
        #takes x and y pos as ints
        count=0
        for x in range(posX-1,posX+2):
            for y in range(posY-1, posY+2):
                if self.isOnBoard(x,y) and self.board[x][y].isMine and (x,y)!=(posX,posY):
                    count+=1
        return count

    def renderBoard(self):
        #renders the board to the screen, uses self.renderDims to get dimensions for rendering the board
        tileWidth=int(self.boardDims.w/self.boardW) #get width and height of each individual tile in pixels
        tileHeight=int(self.boardDims.h/self.boardH) #has to be converted to ints otherwise leaves small gaps on the board

        color=(255,255,255)

        for x in range(self.boardW):
            for y in range(self.boardH):
                xPos=(x*tileWidth)+self.boardDims.x
                yPos=(y*tileHeight)+self.boardDims.x
                r=pygame.Rect(xPos,yPos,tileWidth,tileHeight) #tile rendering rectangle

                #make checkerboard pattern
                if x%2==0:
                    if y%2==0:
                        color=(0,255,0)
                    else:
                        color=(0,0,255)
                else:
                    if y%2==1:
                        color=(0,255,0)
                    else:
                        color=(0,0,255)

                if self.board[x][y].isOpen: 
                    #override color if the tile has already been discovered
                    color=(239,228,176)
                if self.board[x][y].isMine:
                    color=(0,0,0)
                pygame.draw.rect(self.surface,color,r)
                if self.board[x][y].isOpen and self.board[x][y].surroundingMineCount>0:
                    #render text displaying surrounding number of mines on top of tile if tile is open
                    num=255*(self.board[x][y].surroundingMineCount/8)
                    text=self.font.render(str(self.board[x][y].surroundingMineCount),True,(num,num,0))
                    text=pygame.transform.scale(text,(r.w,r.h))
                    self.surface.blit(text,r)
                
                if self.board[x][y].isFlagged:
                    self.surface.blit(self.flagTexture,r)
                


