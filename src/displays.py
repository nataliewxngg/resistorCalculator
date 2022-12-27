import pygame
pygame.init()

def titleText(win,titleFont,white):
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

def buttons(win,titleAndButtonFont,white):
    mouse=pygame.mouse.get_pos() # collects an array of mouse position --> [x,y]

    thirdColor=fourthColor=fifthColor=white
    thirdTextColor=fourthTextColor=fifthTextColor=(190,180,171)

    if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300:
        thirdColor=(190,180,171)
        thirdTextColor=white

    elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: 
        fourthColor=(190,180,171)
        fourthTextColor=white

    elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: 
        fifthColor=(190,180,171)
        fifthTextColor=white

    pygame.draw.rect(win,thirdColor,[420,200,100,100])
    pygame.draw.rect(win,fourthColor,[530,200,100,100]) 
    pygame.draw.rect(win,fifthColor,[640,200,100,100])

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

def description(win,descriptionFont,white):
    descriptionText=descriptionFont.render("bands available",True,white)
    descriptionTextRect=descriptionText.get_rect()
    descriptionTextRect.left=485
    descriptionTextRect.top=305
    win.blit(descriptionText,descriptionTextRect)

def menu(win):
    win.fill((214,206,195))
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))

    titleText(win,pygame.font.Font("assets/GOUDOSB.TTF",60),(255,255,255))

    snowmanImg=pygame.image.load("assets/snowman.png")
    win.blit(snowmanImg,(30,0))

    buttons(win,pygame.font.Font("assets/GOUDOSB.TTF",60),(255,255,255))
    description(win,pygame.font.Font("assets/GOUDOSB.TTF",30),(255,255,255))

def cancelButton(win,cancelColour,cancelFont):
    mouse=pygame.mouse.get_pos()
    # cancelButtonColour=(0,0,0)

    if mouse[0]>20 and mouse[0]<170 and mouse[1]>20 and mouse[1]<60: # if mouse hovers on cancel button, change color
        cancelColour = (190,180,171)

    cancelButton = pygame.draw.rect(win,(214,206,195),[20,20,150,40])

    cancelText = cancelFont.render("return",True,cancelColour)
    win.blit(cancelText,cancelButton)

def calculateButton(win,calculateColor,calculateFont):
    mouse=pygame.mouse.get_pos()
    
    if mouse[0]>320 and mouse[0]<440 and mouse[1]>320 and mouse[1]<360:
        calculateColor=(190,180,171)

    calculateButton=pygame.draw.rect(win,(214,206,195),[320,320,120,40])
    calculateText=calculateFont.render("calculate",True,calculateColor)

    win.blit(calculateText,calculateButton)

# replace with separate pages for different bands
def thirdBand(win,thirdBandColor,fourthBandColor,fifthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))

    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(760/2,340))

        win.blit(ohmText,ohmTextRect)
        
    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>200 and mouse[0]<330 and mouse[1]>90 and mouse[1]<310:
        band1 = pygame.draw.rect(win,(190,180,171),[195,85,120,230])
        hoverOn=1
        
    elif mouse[0]>325 and mouse[0]<435 and mouse[1]>90 and mouse[1]<310:
        band2 = pygame.draw.rect(win,(190,181,171),[320,85,120,230])
        hoverOn=2

    elif mouse[0]>450 and mouse[0]<560 and mouse[1]>90 and mouse[1]<310:
        band3=pygame.draw.rect(win,(190,181,171),[445,85,120,230])
        hoverOn=3

    band1 = pygame.draw.rect(win,thirdBandColor,[200,90,110,220])
    band2 = pygame.draw.rect(win,fourthBandColor,[325,90,110,220])
    band3 = pygame.draw.rect(win,fifthBandColor,[450,90,110,220])

def fourthBand(win,firstBandColor,secondBandColor,thirdBandColor,fourthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))
    
    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(760/2,340))

        win.blit(ohmText,ohmTextRect)

    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>145 and mouse[0]<255 and mouse[1]>90 and mouse[1]<310:
        band1 = pygame.draw.rect(win,(190,180,171),[140,85,120,230])
        hoverOn=1
        
    elif mouse[0]>270 and mouse[0]<380 and mouse[1]>90 and mouse[1]<310:
        band2 = pygame.draw.rect(win,(190,181,171),[265,85,120,230])
        hoverOn=2

    elif mouse[0]>395 and mouse[0]<505 and mouse[1]>90 and mouse[1]<310:
        band3=pygame.draw.rect(win,(190,181,171),[390,85,120,230])
        hoverOn=3

    elif mouse[0]>520 and mouse[0]<630 and mouse[1]>90 and mouse[1]<310:
        band4=pygame.draw.rect(win,(190,181,171),[515,85,120,230])
        hoverOn=4

    band1 = pygame.draw.rect(win,firstBandColor,[145,90,110,220])
    band2 = pygame.draw.rect(win,secondBandColor,[270,90,110,220])
    band3 = pygame.draw.rect(win,thirdBandColor,[395,90,110,220])
    band4 = pygame.draw.rect(win,fourthBandColor,[520,90,110,220])

def fifthBand(win,firstBandColor,secondBandColor,thirdBandColor,fourthBandColor,fifthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))

    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(760/2,340))

        win.blit(ohmText,ohmTextRect)

    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>90 and mouse[0]<200 and mouse[1]>90 and mouse[1]<310:
        band1 = pygame.draw.rect(win,(190,180,171),[85,85,120,230])
        hoverOn=1
        
    elif mouse[0]>215 and mouse[0]<325 and mouse[1]>90 and mouse[1]<310:
        band2 = pygame.draw.rect(win,(190,181,171),[210,85,120,230])
        hoverOn=2

    elif mouse[0]>340 and mouse[0]<505 and mouse[1]>90 and mouse[1]<310:
        band3=pygame.draw.rect(win,(190,181,171),[335,85,120,230])
        hoverOn=3

    elif mouse[0]>465 and mouse[0]<630 and mouse[1]>90 and mouse[1]<310:
        band4=pygame.draw.rect(win,(190,181,171),[460,85,120,230])
        hoverOn=4

    elif mouse[0]>590 and mouse[0]<720 and mouse[1]>90 and mouse[1]<310:
        band4=pygame.draw.rect(win,(190,181,171),[585,85,120,230])
        hoverOn=5

    band1 = pygame.draw.rect(win,firstBandColor,[90,90,110,220])
    band2 = pygame.draw.rect(win,secondBandColor,[215,90,110,220])
    band3 = pygame.draw.rect(win,thirdBandColor,[340,90,110,220])
    band4 = pygame.draw.rect(win,fourthBandColor,[465,90,110,220])
    band5 = pygame.draw.rect(win,fifthBandColor,[590,90,110,220])