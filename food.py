#!/usr/bin/python


import pygame
FOOD_SIZE = 10
FOOD_COLOR = (255,0,0)

class Food:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect =  pygame.Rect((0,0,FOOD_SIZE,FOOD_SIZE))
		self.moveTo(x,y)

	def move(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self,surf):
		
		self.rect.center = (self.x,self.y)
		pygame.draw.rect(surf, FOOD_COLOR, self.rect)

	def hitBy(self,rect):
		return self.rect.colliderect(rect)
		
		
