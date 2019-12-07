import pygame
import random
WEDTH=360
HIGHT=480
FPS=30







WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)



pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption('my game')
clock=pygame.time.Clock()




running=True
while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
                running=False
            


    screen.fill(BLACK)

    
    pygame.display.flip()

pygame.quit()
    
