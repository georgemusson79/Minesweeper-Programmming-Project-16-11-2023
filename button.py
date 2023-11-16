#button.py
import pygame

class Button:
	x=None
	surface=None
	y=None
	h=None
	w=None
	img=None
	rightClickFunc=None
	leftClickFunc=None
	lcArgs=None
	rcArgs=None
	active=True

	def handleClick(self):
		#checks if cursor is colliding with button and handles clicks if the user presses left or right click if button is active, returns void
		x,y=pygame.mouse.get_pos()
		btn=pygame.mouse.get_pressed()
		if self.isColliding(x,y) and self.active:
			if btn[0]:
				self.onLeftClick()
			if btn[1]:
				self.onRightClick()
	def onLeftClick(self):
		#calls leftClickFunc, passing lcArgs if any data is provided, returns 
		if self.leftClickFunc!=None:
			if self.lcArgs==None:
				self.leftClickFunc()
			else:
				self.leftClickFunc(self.lcArgs)
	def onRightClick(self):
		#calls rightClickFunc, passing lcArgs if any data is provided, returns 
		if self.rightClickFunc!=None:
			if self.rcArgs==None:
				self.rightClickFunc()
			else:
				self.rightClickFunc(self.rcArgs)

	def isColliding(self,x,y):
		#takes x and y coordinate for input, check if position collides with button, returns true if so, otherwise returns false
		if (x>=self.x and x<self.x+self.w) and (y>=self.y and y<self.y+self.h):
			return True
		return False

	def setImg(self,imgPath):
		#sets button image to be rendered to the screen, takes a string, returns True on success otherwise returns False and sets self.img to None
		if imgPath!=None or imgPath!="":
			self.img=pygame.image.load(imgPath)
			return True
		self.img=None
		return False

	def renderButton(self):
		#renders button to screen, returns true on success, if button is inactive does nothing and returns false
		if not self.active or self.img==None:
			return False
		dims=pygame.Rect(self.x,self.y,self.w,self.h)
		img=pygame.transform.scale(self.img,(self.w,self.h))
		self.surface.blit(img,(self.x,self.y))
		return True
	
		
	def __init__(self, surface, x, y, w, h, imgPath=None, leftClickFunc=None, rightClickFunc=None, active=True, lcArgs=None, rcArgs=None):
		#button constructor, arguments are: Surface object for rendering, x and y coordinates to place on screen in pixels, width and height in pixels
		#string path to image to be used for button, functions to be used when the button is left clicked and right clicked, bool to determine if button
		#should be useable and left click and right click arguments of any datatype
		self.x=x
		self.y=y
		self.lcArgs=lcArgs
		self.rcArgs=rcArgs
		self.active=active
		self.surface=surface
		self.h=h
		self.w=w
		self.setImg(imgPath)
		self.rightClickFunc=rightClickFunc
		self.leftClickFunc=leftClickFunc


