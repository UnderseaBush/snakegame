#!/usr/bin/python
import pygame
SNAKE_SIZE = 10
SNAKE_COLOR = (0,0,255)


Class Snake:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect((0,0,SNAKE_SIZE,SNAKE_SIZE))
		self.vel = 1 

	def moveUp(self, dt):
		self.y = self.y - self.vel * dt

	def moveDown(self, dt):
		self.y = self.y + self.vel * dt

	def moveLeft(self, dt):
		self.x = self.x-self.vel * dt
	
	def moveRight(self, dt):
		self.x = self.x+ self.vel *dt
		

	def draw(self, surf):
		self.rect.center = (self.x,self.y)
		pygame.draw.rect(surf, SNAKE_COLOR, self.rect)
