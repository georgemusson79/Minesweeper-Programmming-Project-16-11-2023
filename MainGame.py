from cgitb import reset
import pygame
import time
from button import Button
from Tile import Tile
from BoardException import BoardException
import random
import consts
from gameOverOverlay import GameOverOverlay
import gameState
from tkinter import filedialog
import pickle

class MainGame:
    board=None
    flagCounter=0
    boardGenerated=False
    flagTexture:pygame.Surface
    mineCount:int=0
    boardW=0 #represents number of tiles on the board on the x axis
    boardH=0 #represents number of tiles on the board on the y axis
    boardDims=pygame.Rect(0,0,0,0)
    surface=None
    clickCoolDownMaxTime=10 #variables to allow for clicking only after 10 frames have passed since last click
    clickCoolDownTimePassed=0
    font=None #font for rendering numbers to screen
    openCount=0
    gameOver=False
    lose=False
    mineTexture:pygame.Surface
    buttons=[]
    gameOverScreen=None

    def resign(self):
        self.gameOver=True
        self.lose=True
    def exit(self):
        self.reset()
        gameState.setGameState(gameState.GameStates.MAIN_MENU)
        
    def reset(self):
        #clears game over screen and regenerates board with same attributes
        self.openCount=0
        self.gameOverScreen=None
        self.lose=False
        self.gameOver=False
        self.generateBoard(self.boardW,self.boardH,self.mineCount,self.boardDims)
        time.sleep(1)

    def handleGameOver(self):
        #to be called every frame while gameOver is true, handles generation of game over screen and rendering as well as gameOver button inputs
        if self.gameOverScreen==None:
            self.gameOverScreen=GameOverOverlay(self.surface,0,self.surface.get_height()*2,self.lose) #generate game over off screen
            self.gameOverScreen.buttons[0].leftClickFunc=self.reset #sets retry button to regenerate the board on click
            self.gameOverScreen.buttons[1].leftClickFunc=self.exit #quit but when pressed will return to main menu
        if self.gameOverScreen.y>0:
           self.gameOverScreen.y-=self.surface.get_height()/60 #move game over screen upwards into view
            

        self.gameOverScreen.update()
      

    def checkForWin(self):
        #checks every tile to see if its not a mine and not open, if so returns false
        #otherwise it can be assumed that all tiles without mines have been opened and so all mines have been found so returns true
        for x in range(0,self.boardW):
            for y in range(0,self.boardH):
                if not self.board[x][y].isMine and not self.board[x][y].isOpen:
                    return False
        return True

    def openTile(self,x,y):
        #sets tile at x,y position to isOpen if it exists
        #if the surroundingMineCount is 0 on the tile it'll also recursively call openTile() on the surrounding tiles until it finds a tile with a surroundingMineCount greater than 0
        if self.isOnBoard(x,y) and not self.board[x][y].isOpen and not self.board[x][y].isFlagged:
            self.board[x][y].isOpen=True
            if self.board[x][y].isMine:
               #if user left clicks on mine initiate game over
               self.gameOver=True
               self.lose=True
            self.board[x][y].surroundingMineCount=self.getMineCountAroundPt(x,y)
            if (self.board[x][y].surroundingMineCount==0):
                for posX in range(x-1,x+2):
                    for posY in range(y-1,y+2):
                       
                        if (x,y)!=(posX,posY) and self.isOnBoard(posX,posY) and not self.board[posX][posY].isMine:
                            self.openTile(posX,posY)
                            
             
   
    def __init__(self,surface):
        self.surface=surface
        self.font=pygame.font.Font(None,64)

        #generate buttons on bottom left and right of screen
        buttonWidth=surface.get_width()/4
        buttonHeight=surface.get_height()/6
        buttonY=surface.get_height()-buttonHeight
        margin=surface.get_width()/10
        saveButton=Button(surface,margin,buttonY,buttonWidth,buttonHeight,"assets//img//Save.png",self.save)
        exitButton=Button(surface,surface.get_width()-margin-buttonWidth,buttonY,buttonWidth,buttonHeight,"assets//img//resign.png",self.resign)
        self.buttons=[saveButton,exitButton]

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

                if self.checkForWin():
                    #if user has discovered all mines without activating any of them initiate game over by winning
                    self.gameOver=True
                    self.lose=False
                
             
            elif btn[2] and not self.board[boardX][boardY].isOpen: #if right click and tile not opened
                self.board[boardX][boardY].isFlagged= not self.board[boardX][boardY].isFlagged #if flagged becomes not flagged and vice versa
                self.clickCoolDownTimePassed=0
        self.clickCoolDownTimePassed+=1
       
        

    def isOnBoard(self,x:int,y:int):
        #checks if a position is on the board, if so returns true, otherwise returns false
        if x>=0 and x<self.boardW and y>=0 and y<self.boardH:
            return True
        return False

    def setBoardDims(self,x:int,y:int,w:int,h:int):
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
        self.mineTexture=pygame.image.load("assets\\img\\mine.png")
        self.mineTexture=pygame.transform.scale(self.mineTexture,(w/self.boardW,h/self.boardH))

    def generateBoard(self,width:int,height:int,mineCount:int,renderDims:pygame.Rect):
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
        if not self.gameOver:
             self.boardHandleClicks() #only allow the user to open/flag tiles when game is not over
             #only render buttons and allow usage when not game over
             for button in self.buttons:
                button.handleClick() 
                button.render()


        if self.gameOver:
            self.handleGameOver()
   

    def getMineCountAroundPt(self,posX:int,posY:int):
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
                yPos=(y*tileHeight)+self.boardDims.y
                r=pygame.Rect(xPos,yPos,tileWidth,tileHeight) #tile rendering rectangle

                #make checkerboard pattern
                if x%2==0:
                    if y%2==0:
                        color=consts.BOARD_COLOR1
                    else:
                        color=consts.BOARD_COLOR2
                else:
                    if y%2==1:
                        color=consts.BOARD_COLOR1
                    else:
                        color=consts.BOARD_COLOR2

                if self.board[x][y].isOpen: 
                    #override color if the tile has already been discovered
                    color=(239,228,176)
                    if self.board[x][y].isMine:
                        color=(255,0,0) #make tile red if is mine and is open
                pygame.draw.rect(self.surface,color,r)
                if self.board[x][y].isOpen and self.board[x][y].surroundingMineCount>0:
                    #render text displaying surrounding number of mines on top of tile if tile is open
                    num=255*(self.board[x][y].surroundingMineCount/8)
                    text=self.font.render(str(self.board[x][y].surroundingMineCount),True,(num,num,0))
                    text=pygame.transform.scale(text,(r.w,r.h))
                    self.surface.blit(text,r)
                
                if self.board[x][y].isFlagged:
                    self.surface.blit(self.flagTexture,r)
                if self.gameOver and self.lose and self.board[x][y].isMine:
                    #render all mines if game over is true and player has lost
                    self.surface.blit(self.mineTexture,r)

    def save(self):
        #open file explorer and allows user to select and save a file
        #on success returns true otherwise returns false
        try:
            path=filedialog.asksaveasfilename(confirmoverwrite=True,defaultextension=".save",filetypes=[("Minesweeper Save",".save")])
            if path=="":
                return False
            with open(path,"w+b") as file:
                data={"board":self.board,"dims":self.boardDims,"width":self.boardW,"height":self.boardH,"mineCount":self.mineCount,"flagCount":self.flagCounter}
                pickle.dump(data,file)
            return True
        except:
            print("Unable to save the file!")
            return False

    def loadBoardFromFile(self):
        #loads file by get user to select file from file explorer and passing data from file to attributes
        #returns true on success otherwise returns false
        try: 
            path=filedialog.askopenfilename(defaultextension=".save",filetypes=[("Minesweeper Save",".save")])
            if path=="":
                return False
            with open(path,"rb") as file:
                data=pickle.load(file)
                self.board=data["board"]
                dims=data["dims"]
                self.setBoardDims(dims.x,dims.y,dims.w,dims.h)
                self.boardW=data["width"]
                self.boardH=data["height"]
                self.mineCount=data["mineCount"]
                self.flagCounter=data["flagCount"]
                self.boardGenerated=True
                return True
        except:
            print("Unable to load the file!")
            return False

         

                      