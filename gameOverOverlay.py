from cProfile import label
import pygame
import consts
from label import Label
from button import Button
class GameOverOverlay:
    buttons=[]
    x:int
    y:int
    lose:bool #for displaying different text based on win/loss
    gameOverLabel:Label
    bg:pygame.Surface #background
    gameOverBox:pygame.Surface #box containing game over text and buttons
    surface:pygame.Surface



    def render(self):
        centreX=self.surface.get_width()/2
        centreY=self.surface.get_height()/2
        gameOverBoxX=centreX-(self.gameOverBox.get_width()/2)+self.x
        gameOverBoxY=centreY-(self.gameOverBox.get_height()/2)+self.y
        self.surface.blit(self.bg,(self.x,self.y))
        self.surface.blit(self.gameOverBox,(gameOverBoxX,gameOverBoxY))

        #position buttons so they are in the bottom left and bottom right corners of the game over box
        marginX=self.gameOverBox.get_width()/10
        marginY=self.gameOverBox.get_height()/10
        buttonsY=gameOverBoxY+self.gameOverBox.get_height()-self.buttons[0].h-marginY
        self.buttons[0].x=gameOverBoxX+marginX
        self.buttons[1].x=gameOverBoxX+self.gameOverBox.get_width()-self.buttons[1].w-marginX
        for button in self.buttons:
            button.y=buttonsY
            button.render()


        self.gameOverLabel.x=(centreX-self.gameOverLabel.w/2)+self.x
        self.gameOverLabel.y=gameOverBoxY+self.gameOverBox.get_height()/10
        self.gameOverLabel.render()


    def __init__(self,surface:pygame.Surface,x:int,y,lose:bool):
        #generates a game over screen with a grey background the size of the entire screen with a box in the centre with text and buttons
        self.x=x
        self.y=y
        self.surface=surface
        self.lose=lose
        self.bg=pygame.Surface((surface.get_width(),surface.get_height()))
        self.bg.set_alpha(128)
        self.bg.fill(consts.GAMEOVER_BG_COLOR)
        self.gameOverBox=pygame.image.load("assets//img//gameOverBox.png")
        self.gameOverBox=pygame.transform.scale(self.gameOverBox,(surface.get_width()*0.75,surface.get_height()*0.75)) #scale box to be 2/3rds the width and height of the window
        if lose:
            text="Game Over!You lose."
        else:
            text="Game Over!You Win."
        self.gameOverLabel=Label(surface,0,0,self.gameOverBox.get_width()*0.75,self.gameOverBox.get_height()/2,text,lineCharLimit=len("Game Over!"))

        #generate buttons and add to buttons list
        retryButton=Button(surface,0,0,self.gameOverBox.get_width()*0.35,self.gameOverBox.get_height()*0.25,"assets//img//retry.png")
        quitButton=Button(surface,0,0,self.gameOverBox.get_width()*0.35,self.gameOverBox.get_height()*0.25,"assets//img//quit.png")
        self.buttons=[retryButton,quitButton]





