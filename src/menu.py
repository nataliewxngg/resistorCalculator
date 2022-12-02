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

def selectMenu(win,white,cancelColor): 
    win.fill(white)
    mouse=pygame.mouse.get_pos()
    if mouse[0]>350 and mouse[0]<450 and mouse[1]>300 and mouse[1]<350: 
        cancelColour=(0,0,0)
    cancelButton=pygame.draw.rect(win,cancelColor,[350,300,100,50])
