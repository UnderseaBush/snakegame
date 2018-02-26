#Might be cool to use a potentiometer to increase or decrease speed level of game. 
#Maybe make a timer for powerups to be displayed only for a certain time
#

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

SPEED = 2
FPS = 30

GREY = (128, 128, 128)
RED = (255, 0, 0)
my_food = food.Food(random.random()*400, random.random()*400) #May be a good idea to use a graphic or something to signify that this is food. Maybe make a legend in the game screen for your snake, food, etc!
my_snake = snake.Snake(random.random()*400, random.random()*400)

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	window = pygame.display.set_mode((WinWIDTH, WinHEIGHT), 0, 32)
	pygame.display.set_caption('SNAKE')

	while(True):

		#Events
		for event in pygame.event.get():
			#kEY events
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					my_snake.moveUp(SPEED)
					print 'up arrow'
				if event.key == pygame.K_DOWN:
					my_snake.moveDown(SPEED*-1) #Good idea to make things less complicated
				if event.key == pygame.K_RIGHT:
					my_snake.moveRight(SPEED)
				if event.key == pygame.K_LEFT:
					my_snake.moveLeft(SPEED*-1)
				if event.key == pygame.K_SPACE:
					my_snake.move(1.0/FPS)

			#QUIT event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

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
