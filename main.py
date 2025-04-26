import pygame 
from checkers.constants import *
from checkers.game import Board

FBS = 60
Win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Checkers Game')


def main():
    run = True
    clock = pygame.time.Clock() 
    new_board = Board()

    while run:
        clock.tick(FBS)
        for event in pygame.event.get(): #Check if the user close the window
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        new_board.draw(Win)
        pygame.display.update()
        
    pygame.quit()
main()