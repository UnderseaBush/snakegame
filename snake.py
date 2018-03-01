#!/usr/bin/python
import pygame
SNAKE_SIZE = 10
SNAKE_COLOR = (0,255,0)


class Snake:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect((0,0,SNAKE_SIZE,SNAKE_SIZE))
		self.vel = 50

	def move(self, time, x, y):
		self.vel_x = x
		self.vel_y = y
		self.x = self.x + self.vel_x*time
		self.y = self.y + self.vel_y*time


	def draw(self, surf):
		self.rect.center = (self.x,self.y)
		pygame.draw.rect(surf, SNAKE_COLOR, self.rect)
