#!/usr/bin/python
import pygame, sys
import serial
from pygame.locals import *
#import snake
#import food

WinWIDTH = 500
WinHEIGHT = 480

GREY = (128, 128, 128)

def main():
	pygame.init
	fpsClock = pygame.time.Clock()
	window = pygame.display.set_mode((WinWIDTH, WinHEIGHT), 0, 32)
	pygame.display.set_caption('SNAKE')
	
	while(True):
	
		#Events
		for event in pygame.event.get():
			#kEY events
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					#TODO remaining key events
					
			#QUIT event
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
		#Update Display
		drawWorld(window)
		pygame.display.update()
		
def drawWorld(surf):
	surf.fill(GREY)

if __name__=="__main__":
	main()
