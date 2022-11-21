# from src.backEnd import resistorCalculator
import pygame

# initiation
pygame.init()
win=pygame.display.set_mode((800,400))
pygame.display.set_caption("Resistor Calculator")
running=True

# colors
white=(255,255,255)

# menu
def menuTitleText():
    titleFont=pygame.font.Font("assets/GOUDOSB.TTF",60)

    resistorText=titleFont.render("RESISTOR",True,white)
    resistorTextRect=resistorText.get_rect()
    resistorTextRect.left=300
    resistorTextRect.top=50
    win.blit(resistorText,resistorTextRect)

    calculatorText=titleFont.render("CALCULATOR",True,white)
    calculatorTextRect=calculatorText.get_rect()
    calculatorTextRect.left=340
    calculatorTextRect.top=100
    win.blit(calculatorText,calculatorTextRect)

def menuButtons():
    mouse=pygame.mouse.get_pos()
    thirdColor=white
    fourthColor=white
    fifthColor=white

    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300:
        thirdColor=(0,0,0)

    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300:
        fourthColor=(0,0,0)
    
    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300:
        fifthColor=(0,0,0)

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
    mouse=pygame.mouse.get_pos()
    win.fill((214,206,195))
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))

    menuTitleText()

    snowmanImg=pygame.image.load("assets/snowman.png")
    win.blit(snowmanImg,(30,0))

    menuButtons()
    menuDescription()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  

    menu()
    pygame.display.update()
    