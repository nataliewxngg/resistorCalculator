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

    if mouse[0]>20 and mouse[0]<110 and mouse[1]>20 and mouse[1]<60: # if mouse hovers on cancel button, change color
        cancelColour = (190,180,171)

    cancelButton = pygame.draw.rect(win,(214,206,195),[20,20,10,40])

    cancelText = cancelFont.render("return",True,cancelColour)
    win.blit(cancelText,cancelButton)

def calculateButton(win,calculateColor,calculateFont):
    mouse=pygame.mouse.get_pos()
    
    if mouse[0]>360 and mouse[0]<440 and mouse[1]>310 and mouse[1]<335:
        calculateColor=(190,180,171)

    calculateText=calculateFont.render("calculate",True,calculateColor)
    calculateTextRect=calculateText.get_rect(center=(800/2,325))

    win.blit(calculateText,calculateTextRect)

# replace with separate pages for different bands
def thirdBand(win,thirdBandColor,fourthBandColor,fifthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    bgImg=pygame.image.load("assets/threeBandsBg.png")
    win.blit(bgImg,(0,0))
    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))

    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",20))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(800/2,325))

        win.blit(ohmText,ohmTextRect)
        
    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>220 and mouse[0]<330 and mouse[1]>85 and mouse[1]<305:
        band1Shadow = pygame.draw.rect(win,(190,180,171),[215,80,120,230])
        hoverOn=1
        
    elif mouse[0]>345 and mouse[0]<455 and mouse[1]>85 and mouse[1]<305:
        band2Shadow = pygame.draw.rect(win,(190,181,171),[340,80,120,230])
        hoverOn=2

    elif mouse[0]>470 and mouse[0]<580 and mouse[1]>85 and mouse[1]<305:
        band3Shadow=pygame.draw.rect(win,(190,181,171),[465,80,120,230])
        hoverOn=3

    band1 = pygame.draw.rect(win,thirdBandColor,[220,85,110,220])
    band2 = pygame.draw.rect(win,fourthBandColor,[345,85,110,220])
    band3 = pygame.draw.rect(win,fifthBandColor,[470,85,110,220])

def fourthBand(win,firstBandColor,secondBandColor,thirdBandColor,fourthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    bgImg=pygame.image.load("assets/fourBandsBg.png")
    win.blit(bgImg,(0,0))

    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))
    
    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",20))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(800/2,325))

        win.blit(ohmText,ohmTextRect)

    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>160 and mouse[0]<270 and mouse[1]>90 and mouse[1]<310:
        band1Shadow = pygame.draw.rect(win,(190,180,171),[155,85,120,230])
        hoverOn=1
        
    elif mouse[0]>285 and mouse[0]<395 and mouse[1]>90 and mouse[1]<310:
        band2Shadow = pygame.draw.rect(win,(190,181,171),[280,85,120,230])
        hoverOn=2

    elif mouse[0]>410 and mouse[0]<520 and mouse[1]>90 and mouse[1]<310:
        band3Shadow=pygame.draw.rect(win,(190,181,171),[405,85,120,230])
        hoverOn=3

    elif mouse[0]>535 and mouse[0]<645 and mouse[1]>90 and mouse[1]<310:
        band4Shadow=pygame.draw.rect(win,(190,181,171),[530,85,120,230])
        hoverOn=4

    band1 = pygame.draw.rect(win,firstBandColor,[160,90,110,220])
    band2 = pygame.draw.rect(win,secondBandColor,[285,90,110,220])
    band3 = pygame.draw.rect(win,thirdBandColor,[410,90,110,220])
    band4 = pygame.draw.rect(win,fourthBandColor,[535,90,110,220])

def fifthBand(win,firstBandColor,secondBandColor,thirdBandColor,fourthBandColor,fifthBandColor,white,calculated,ohm,ohmFont):
    win.fill((214,206,195))
    bgImg=pygame.image.load("assets/fiveBandsBg.png")
    win.blit(bgImg,(0,0))

    cancelButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",35))

    if calculated==False:
        calculateButton(win,white,pygame.font.Font("assets/GOUDOSB.TTF",20))
    else:
        ohmText=ohmFont.render(ohm,True,white)
        ohmTextRect=ohmText.get_rect(center=(800/2,325))

        win.blit(ohmText,ohmTextRect)

    hoverOn=0
    mouse=pygame.mouse.get_pos()

    # can simplify by getting mouse first, then check if button is clicked
    if mouse[0]>90 and mouse[0]<205 and mouse[1]>90 and mouse[1]<310:
        band1 = pygame.draw.rect(win,(190,180,171),[90,85,120,230])
        hoverOn=1
        
    elif mouse[0]>215 and mouse[0]<330 and mouse[1]>90 and mouse[1]<310:
        band2 = pygame.draw.rect(win,(190,181,171),[215,85,120,230])
        hoverOn=2

    elif mouse[0]>340 and mouse[0]<455 and mouse[1]>90 and mouse[1]<310:
        band3=pygame.draw.rect(win,(190,181,171),[340,85,120,230])
        hoverOn=3

    elif mouse[0]>465 and mouse[0]<580 and mouse[1]>90 and mouse[1]<310:
        band4=pygame.draw.rect(win,(190,181,171),[465,85,120,230])
        hoverOn=4

    elif mouse[0]>590 and mouse[0]<705 and mouse[1]>90 and mouse[1]<310:
        band4=pygame.draw.rect(win,(190,181,171),[590,85,120,230])
        hoverOn=5

    band1 = pygame.draw.rect(win,firstBandColor,[95,90,110,220])
    band2 = pygame.draw.rect(win,secondBandColor,[220,90,110,220])
    band3 = pygame.draw.rect(win,thirdBandColor,[345,90,110,220])
    band4 = pygame.draw.rect(win,fourthBandColor,[470,90,110,220])
    band5 = pygame.draw.rect(win,fifthBandColor,[595,90,110,220])