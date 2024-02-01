#Download pygame library first then import 
import pygame
import sys
import random

#Initialize a game 
pygame.init()

#Set frame rate
clock = pygame.time.Clock()
fps = 60

#Dimensions of the window 
bottom_panel = 200
WIDTH = 800
HEIGHT = 400 + bottom_panel


screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Create game name 
pygame.display.set_caption('Assignement 3 - Battle Game')

#Load images 
#Backgournd image 
background_img = pygame.image.load('Battle Game/img/Background/background.png').convert_alpha()
#Panel image 
panel_img = pygame.image.load('Battle Game/img/Panel/panel.png').convert_alpha()


#Function for drawing backgorund 
def draw_bg():
    screen.blit(background_img, (0,0))

#Function for drawing panel 
def draw_panel():
     screen.blit(panel_img, (0,HEIGHT - bottom_panel))

#fighter class
class Fighter():
    def_init_(self,x,y,name,max_hp, strength, potions, lives):
    self.name = name 
    self.max_hp 
    self.hp = max_hpself.strength = strength 
    self.start_potions = potionsself.potions = potions
    self.lives = lives 
    self.alive = True 
    self.image = pygame.image.load()


run = True 
while run:

    clock.tick(fps)

    #Draw backgournd 
    draw_bg()

    #Draw panel 
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 

    pygame.display.update()

pygame.quit()
sys.exit()