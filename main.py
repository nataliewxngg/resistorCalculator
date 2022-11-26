# from src.backEnd import resistorCalculator
import pygame
from src.displays import displays

# initiation
pygame.init() # initializes all pygame modules
pygame.display.set_caption("Resistor Calculator")
running=True

# main program
while running:
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            running=False

    game=displays(pygame.display.set_mode((800,400)))
    game.menu()
    pygame.display.update() 
    