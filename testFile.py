from src.menu import menu
import pygame

running=True
win=pygame.display.set_mode((800,400))

while running:
    for event in pygame.event.get(): # goes through events from module
        if event.type==pygame.QUIT: # if user closes win
            running=False # program stops
        
    menu(win)
    pygame.display.update()