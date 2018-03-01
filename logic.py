#!/usr/bin/python
import pygame, sys
import serial
from pygame.locals import *
import time
import random
import snake
import food

WinWIDTH = 500
WinHEIGHT = 480

SPEED = 30
FPS = 60


GREY = (128, 128, 128)
RED = (255, 0, 0)
my_food = food.Food(random.random()*400, random.random()*400)
my_snake = snake.Snake(random.random()*400, random.random()*400)

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	window = pygame.display.set_mode((WinWIDTH, WinHEIGHT), 0, 32)
	pygame.display.set_caption('SNAKE')
	START = False
	Xdir = 0
	Ydir = 0

	while(True):

		#Events
		for event in pygame.event.get():
			#kEY events
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					Ydir = -SPEED
					Xdir = 0
				if event.key == pygame.K_DOWN:
					Ydir = SPEED
					Xdir = 0
				if event.key == pygame.K_RIGHT:
					Ydir = 0
					Xdir = SPEED
				if event.key == pygame.K_LEFT:
					Ydir = 0
					Xdir = -SPEED
				if event.key == pygame.K_SPACE:
					Xdir = SPEED
					Ydir = 0
					START = True

			#QUIT event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		#Game Logic
		if START:
			my_snake.move(1.0/FPS, Xdir, Ydir)

		#Update Display
		drawWorld(window)
		my_food.draw(window)
		my_snake.draw(window)

		pygame.display.update()
		fpsClock.tick(FPS)

def drawWorld(surf):
	surf.fill(GREY)

def Message(surf, msg):
	#display GAME OVER and WINNER
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfObj = fontObj.render(msg, True, RED)
	textRectObj = textSurfObj.get_rect()
	textRectObj.center = (WinWIDTH/2, WinHEIGHT/2)
	surf.blit(textSurfObj,textRectObj)
	pygame.display.update()
	time.sleep(1)

if __name__=="__main__":
	main()
