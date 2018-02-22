#!/usr/bin/python
import pygame
SNAKE_SIZE = 10
SNAKE_COLOR = (0,255,0)


class Snake:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.v_x = 1
		self.rect = pygame.Rect((0,0,SNAKE_SIZE,SNAKE_SIZE))
		self.vel = 1

	def move(self, time):
		self.x = self.x + self.v_x*time

	def moveUp(self, dt):
		self.y = self.y - self.vel * dt

	def moveDown(self, dt):
		self.y = self.y + self.vel * (-dt)

	def moveLeft(self, dt):
		self.x = self.x-self.vel * (-dt)

	def moveRight(self, dt):
		self.x = self.x+ self.vel *dt


	def draw(self, surf):
		self.rect.center = (self.x,self.y)
		pygame.draw.rect(surf, SNAKE_COLOR, self.rect)
