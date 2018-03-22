#!/usr/bin/python
import pygame, sys
import serial
from pygame.locals import *
import time
import random
import snake
import food

WinWIDTH = 300
WinHEIGHT = 280


FPS = 60

strTime = '5'

GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 100)
GREEN = (0, 255, 0)
my_food = food.Food(random.random()*WinWIDTH, random.random()*WinHEIGHT)
my_snake = snake.Snake(random.random()*WinWIDTH, random.random()*WinHEIGHT)
my_time = snake.Timer()


def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	window = pygame.display.set_mode((WinWIDTH, WinHEIGHT), 0, 32)
	pygame.display.set_caption('SNAKE')
	START = False
	Xdir = 0
	Ydir = 0
	score = -1
	SPEED = 30

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
					Message(window, 'GO!', BLUE)

				if event.key == pygame.K_k:
					Timer()

			#QUIT event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		#Game Logic
		if START:
			Timer()
			my_snake.move(1.0/FPS, Xdir, Ydir)
			print "Class", my_time.time
			#Message(window, strTime, GREEN)

		if BoxBounds():
			Message(window, 'FAIL', RED)

		if my_food.hitBy(my_snake):
			my_food.x = random.random()*WinWIDTH
			my_food.y = random.random()*WinHEIGHT
			score = score + 1
			SPEED = SPEED + 10
			

		#Update Display
		drawWorld(window)
		my_food.draw(window)
		my_snake.draw(window)
		DisplayScore(window, str(score))
		pygame.display.update()
		fpsClock.tick(FPS)

def drawWorld(surf):
	surf.fill(GREY)

def Message(surf, msg, clr):
	#display GAME OVER and WINNER
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfObj = fontObj.render(msg, True, clr)
	textRectObj = textSurfObj.get_rect()
	textRectObj.center = (WinWIDTH/2, WinHEIGHT/2)
	surf.blit(textSurfObj,textRectObj)
	pygame.display.update()
	time.sleep(1)



def DisplayScore(surf, score):
	
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfObj = fontObj.render(score, True, BLUE)
	textRectObj = textSurfObj.get_rect()
	textRectObj.center = (WinWIDTH-25, WinHEIGHT-25)
	surf.blit(textSurfObj,textRectObj)
	
	


def BoxBounds():
	if (my_snake.x>WinWIDTH)or(my_snake.x<0)or(my_snake.y>WinHEIGHT)or(my_snake.y<0):
		return True
	else:
		return False

def Timer():
	time = pygame.time.get_ticks()/1000
	print time


if __name__=="__main__":
	main()
