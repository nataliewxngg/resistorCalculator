import pygame

class displays:
    def __init__(self,win):
        self.win=win
        self,win.fill((214,206,195))
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))

        self.titleAndButtonFont=pygame.font.Font("assets/GOUDOSB.TTF",60)
        self.descriptionFont=pygame.font.Font("assets/GOUDOSB.TTF",30)

        self.white=(255,255,255)
        self.mouse=pygame.mouse.get_pos()

    def menu(self):
        snowmanImg=pygame.image.load("assets/snowman.png")
        self.win.blit(snowmanImg,(30,0))

        # menuTitleText        
        resistorText=self.titleAndButtonFont.render("RESISTOR",True,self.white)
        resistorTextRect=resistorText.get_rect()
        resistorTextRect.left=300
        resistorTextRect.top=50
        self.win.blit(resistorText,resistorTextRect)

        calculatorText=self.titleAndButtonFont.render("CALCULATOR",True,self.white)
        calculatorTextRect=calculatorText.get_rect()
        calculatorTextRect.left=340
        calculatorTextRect.top=100
        self.win.blit(calculatorText,calculatorTextRect)

        # menuButtons
        thirdButtonColor=fourthButtonColor=fifthButtonColor=self.white
        thirdTextColor=fourthTextColor=fifthTextColor=(190,180,171)

        if self.mouse[0]>420 and self.mouse[0]<520 and self.mouse[1]>200 and self.mouse[1]<300: # if mouse hovers in boundaries of first button's rect
            thirdButtonColor=(190,180,171)
            thirdTextColor=self.white

        elif self.mouse[0]>530 and self.mouse[0]<630 and self.mouse[1]>200 and self.mouse[1]<300: # if mouse hovers in boundaries of ... rect
            fourthButtonColor=(190,180,171)
            fourthTextColor=self.white
        
        elif self.mouse[0]>640 and self.mouse[0]<740 and self.mouse[1]>200 and self.mouse[1]<300: # if mouse hovers in boundaries of ... rect
            fifthButtonColor=(190,180,171)
            fifthTextColor=self.white

        buttonThree=pygame.draw.rect(self.win,thirdButtonColor,[420,200,100,100])
        buttonFour=pygame.draw.rect(self.win,fourthButtonColor,[530,200,100,100]) 
        buttonFive=pygame.draw.rect(self.win,fifthButtonColor,[640,200,100,100])
        
        buttonThreeText=self.titleAndButtonFont.render("3",True,thirdTextColor)
        buttonThreeTextRect=buttonThreeText.get_rect()
        buttonThreeTextRect.left=455
        buttonThreeTextRect.top=215
        self.win.blit(buttonThreeText,buttonThreeTextRect)

        buttonFourText=self.titleAndButtonFont.render("4",True,fourthTextColor)
        buttonFourTextRect=buttonFourText.get_rect()
        buttonFourTextRect.left=565
        buttonFourTextRect.top=215
        self.win.blit(buttonFourText,buttonFourTextRect)

        buttonFiveText=self.titleAndButtonFont.render("5",True,fifthTextColor)
        buttonFiveTextRect=buttonFiveText.get_rect()
        buttonFiveTextRect.left=675
        buttonFiveTextRect.top=215
        self.win.blit(buttonFiveText,buttonFiveTextRect)

        # menuDescription
        descriptionText=self.descriptionFont.render("bands available",True,self.white) 
        descriptionTextRect=descriptionText.get_rect()
        descriptionTextRect.left=485
        descriptionTextRect.top=305
        self.win.blit(descriptionText,descriptionTextRect)
