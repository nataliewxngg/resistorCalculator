# from src.backEnd import resistorCalculator
import pygame

# initiation
pygame.init() # initializes all pygame modules
win=pygame.display.set_mode((800,400))
pygame.display.set_caption("Resistor Calculator")
running=True

# colors
white=(255,255,255)

# menu
def menuTitleText():
    titleFont=pygame.font.Font("assets/GOUDOSB.TTF",60) # initiates font family and style for future uses

    resistorText=titleFont.render("RESISTOR",True,white) # RESISTOR text on menu
    resistorTextRect=resistorText.get_rect() # rect(angle) to store the text
    resistorTextRect.left=300
    resistorTextRect.top=50
    win.blit(resistorText,resistorTextRect) # adds the arguments on to win

    calculatorText=titleFont.render("CALCULATOR",True,white) # CALCULATOR text on menu
    calculatorTextRect=calculatorText.get_rect() # rect(angle) to store the text
    calculatorTextRect.left=340
    calculatorTextRect.top=100
    win.blit(calculatorText,calculatorTextRect) # adds the arguments on to win

def menuButtons():
    mouse=pygame.mouse.get_pos() # collects an array of mouse position --> [x,y]

    thirdColor=white
    fourthColor=white
    fifthColor=white

    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of first button's rect
        thirdColor=(0,0,0)

    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of ... rect
        fourthColor=(0,0,0)
    
    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of ... rect
        fifthColor=(0,0,0)

    # display colors of buttons depending on mouse positions
    buttonThree=pygame.draw.rect(win,thirdColor,[420,200,100,100])
    buttonFour=pygame.draw.rect(win,fourthColor,[530,200,100,100]) 
    buttonFive=pygame.draw.rect(win,fifthColor,[640,200,100,100])

def menuDescription():
    descriptionFont=pygame.font.Font("assets/GOUDOSB.TTF",30)

    descriptionText=descriptionFont.render("bands available",True,white)
    descriptionTextRect=descriptionText.get_rect()
    descriptionTextRect.left=485
    descriptionTextRect.top=305
    win.blit(descriptionText,descriptionTextRect)

def menu():
    win.fill((214,206,195))
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))

    menuTitleText()

    snowmanImg=pygame.image.load("assets/snowman.png")
    win.blit(snowmanImg,(30,0))

    menuButtons()
    menuDescription()

# main program
while running:
    for event in pygame.event.get(): # goes through events from module
        if event.type==pygame.QUIT: # if user closes win
            running=False # program stops

    menu()
    pygame.display.update() # finally updates the win to show all the .blit(ing)
    