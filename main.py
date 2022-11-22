# from src.backEnd import resistorCalculator
import pygame
import time

# initiation
pygame.init() # initializes all pygame modules
win=pygame.display.set_mode((800,400))
pygame.display.set_caption("Resistor Calculator")
running=True

# fonts
titleAndButtonFont=pygame.font.Font("assets/GOUDOSB.TTF",60)

# colors
white=(255,255,255)

# menu
def menuTitleText():

    resistorText=titleAndButtonFont.render("RESISTOR",True,white) # RESISTOR text on menu
    resistorTextRect=resistorText.get_rect() # rect(angle) to store the text
    resistorTextRect.left=300
    resistorTextRect.top=50
    win.blit(resistorText,resistorTextRect) # adds the arguments on to win

    calculatorText=titleAndButtonFont.render("CALCULATOR",True,white) # CALCULATOR text on menu
    calculatorTextRect=calculatorText.get_rect() # rect(angle) to store the text
    calculatorTextRect.left=340
    calculatorTextRect.top=100
    win.blit(calculatorText,calculatorTextRect) # adds the arguments on to win

def menuButtons():
    mouse=pygame.mouse.get_pos() # collects an array of mouse position --> [x,y]

    thirdButtonColor=fourthButtonColor=fifthButtonColor=white
    thirdTextColor=fourthTextColor=fifthTextColor=(190,180,171)

    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of first button's rect
        thirdButtonColor=(190,180,171)
        thirdTextColor=white

    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of ... rect
        fourthButtonColor=(190,180,171)
        fourthTextColor=white
    
    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: # if mouse hovers in boundaries of ... rect
        fifthButtonColor=(190,180,171)
        fifthTextColor=white

    # display colors of buttons depending on mouse positions
    buttonThree=pygame.draw.rect(win,thirdButtonColor,[420,200,100,100])
    buttonFour=pygame.draw.rect(win,fourthButtonColor,[530,200,100,100]) 
    buttonFive=pygame.draw.rect(win,fifthButtonColor,[640,200,100,100])
    
    buttonThreeText=titleAndButtonFont.render("3",True,thirdTextColor)
    buttonThreeTextRect=buttonThreeText.get_rect()
    buttonThreeTextRect.left=455
    buttonThreeTextRect.top=215
    win.blit(buttonThreeText,buttonThreeTextRect)

    buttonFourText=titleAndButtonFont.render("4",True,fourthTextColor)
    buttonFourTextRect=buttonFourText.get_rect()
    buttonFourTextRect.left=565
    buttonFourTextRect.top=215
    win.blit(buttonFourText,buttonFourTextRect)

    buttonFiveText=titleAndButtonFont.render("5",True,fifthTextColor)
    buttonFiveTextRect=buttonFiveText.get_rect()
    buttonFiveTextRect.left=675
    buttonFiveTextRect.top=215
    win.blit(buttonFiveText,buttonFiveTextRect)

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
    