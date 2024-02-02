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
    def __init__(self, x, y, name, max_hp, strength, potions, lives):
        self.name = name 
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength 
        self.start_potions = potions
        self.lives = lives 
        self.alive = True 
        img = pygame.image.load(f'Battle Game/img/{self.name}/animation/Idle/idle_1.png')
        self.image = pygame.transform.scale(img, (img.get_width()/3, img.get_height()/3)) #This line is added in to reduce the size of the images as they too big 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

knight = Fighter(100, 260, 'Knight', 30, 10, 3, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

run = True 
while run:

    clock.tick(fps)

    #Draw backgournd 
    draw_bg()

    #Draw panel 
    draw_panel()

    #Draw fighters 
    knight.draw()
    for bandit in bandit_list:
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 

    pygame.display.update()

pygame.quit()
sys.exit()