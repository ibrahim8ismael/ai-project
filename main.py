import pygame 
from checkers.constants import *

FBS = 60
Win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers Game')


def main():
    run = True
    clock = pygame.time.Clock() 

    while run:
        clock.tick(FBS)
        for event in pygame.event.get(): #Check if the user close the window
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.quit()
main()