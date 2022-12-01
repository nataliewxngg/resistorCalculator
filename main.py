# from src.backEnd import resistorCalculator 
import pygame
from src.menu import menu

# initiation
pygame.init() # initializes all pygame modules
win=pygame.display.set_mode((800,400))

running=True
mouse=pygame.mouse.get_pos()
white=(255,255,255)

# SDLKFJASDLKFJWEPOAIFJSDOIFJASDP CODE
chosen = 0 # which square was clicked?
windowType = 0 # 0 means the main menu is open, 1 means selecting colour menu is open

def selectMenu(): # changes the menu to selecting a colour
    win.fill(white)
    cancelColour = (100, 100, 100)
    mouse=pygame.mouse.get_pos()
    if mouse[0]>350 and mouse[0]<450 and mouse[1]>300 and mouse[1]<350: 
        cancelColour=(0,0,0)
    cancelButton=pygame.draw.rect(win,cancelColour,[350,300,100,50])

def chooseBand() : # check if one of the squares is clicked on
    global chosen
    chosen = 0
    mouse=pygame.mouse.get_pos()
    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300: 
        chosen = 3
    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: 
        chosen = 4
    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: 
        chosen = 5
    if chosen == 0: return # if the click was not on any squares
    global windowType
    windowType = 1

def chooseColour(): #check if a colour is chosen, or if the cancel button is pressed
    mouse=pygame.mouse.get_pos()
    if mouse[0]>350 and mouse[0]<450 and mouse[1]>300 and mouse[1]<350: 
        global windowType
        windowType = 0

# main program
while running:
    for event in pygame.event.get(): # goes through events from module
        if event.type==pygame.QUIT: # if user closes win
            running=False # program stop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if windowType == 0: 
                chooseBand()
            elif windowType == 1: 
                chooseColour()

    if windowType == 0: 
        menu(win)
    elif windowType == 1: 
        selectMenu()
    pygame.display.update() 