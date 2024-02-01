#Download pygame library first then import 
import pygame
import sys
import random

#Initialize a game 
pygame.init()

#Dimensions of the window 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Create game name 
pygame.display.set_caption('Assignement 3 - Battle Game')

run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 

