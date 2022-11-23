# from src.backEnd import resistorCalculator
import pygame
from src.displays import displays

# initiation
pygame.init() # initializes all pygame modules
pygame.display.set_caption("Resistor Calculator")
running=True

# main program
while running:
    for event in pygame.event.get(): # goes through events from module
        if event.type==pygame.QUIT: # if user closes win
            running=False # program stops

    game=displays(pygame.display.set_mode((800,400)))
    game.menu()
    pygame.display.update() # finally updates the win to show all the .blit(ing)
    