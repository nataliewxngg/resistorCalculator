import pygame

class displays:
    def __init__(self,win):
        pygame.init()
        self.win=win
        self.win.fill((214,206,195))
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))

        self.titleAndButtonFont=pygame.font.Font("assets/GOUDOSB.TTF",60)
        self.descriptionFont=pygame.font.Font("assets/GOUDOSB.TTF",30)

        self.white=(255,255,255)
        self.mouse=pygame.mouse.get_pos()

    def threeBandsDisplay(self):
        exit=False
        while exit==False:
            self.win.fill((0,0,0))
            pygame.display.update() 
    
    def fourBandsDisplay(self):
        exit=False
        while exit==False:
            self.win.fill((108,108,108))
            pygame.display.update()
    
    def fiveBandsDisplay(self):
        exit=False
        while exit==False:
            self.win.fill((255,255,255))
            pygame.display.update()

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
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    game=displays(self.win)
                    game.threeBandsDisplay()
                    break

        elif self.mouse[0]>530 and self.mouse[0]<630 and self.mouse[1]>200 and self.mouse[1]<300: # if mouse hovers in boundaries of ... rect
            fourthButtonColor=(190,180,171)
            fourthTextColor=self.white
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    game=displays(self.win)
                    game.fourBandsDisplay()
                    break
        
        elif self.mouse[0]>640 and self.mouse[0]<740 and self.mouse[1]>200 and self.mouse[1]<300: # if mouse hovers in boundaries of ... rect
            fifthButtonColor=(190,180,171)
            fifthTextColor=self.white
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    game=displays(self.win)
                    game.fiveBandsDisplay()
                    break

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

    def selectMenu(self): # changes the menu to selecting a colour
        self.win.fill((255, 255, 255))
        cancelColour = (100, 100, 100)
        mouse=pygame.mouse.get_pos()
        if mouse[0]>350 and mouse[0]<450 and mouse[1]>300 and mouse[1]<350: cancelColour=(0,0,0)
        cancelButton=pygame.draw.rect(self.win,cancelColour,[350,300,100,50])

    def chooseBand(self) : # check if one of the squares is clicked on
        global chosen
        chosen = 0
        mouse=pygame.mouse.get_pos()
        if mouse[0]>420 and mouse[0]<520 and mouse[1]>200 and mouse[1]<300: chosen = 3
        elif mouse[0]>530 and mouse[0]<630 and mouse[1]>200 and mouse[1]<300: chosen = 4
        elif mouse[0]>640 and mouse[0]<740 and mouse[1]>200 and mouse[1]<300: chosen = 5
        if chosen == 0: return # if the click was not on any squaresd
        global windowType
        windowType = 1

    def chooseColour(self): #check if a colour is chosen, or if the cancel button is pressed
        mouse=pygame.mouse.get_pos()
        if mouse[0]>350 and mouse[0]<450 and mouse[1]>300 and mouse[1]<350: 
            global windowType
            windowType = 0


#ppeeepeeepoopoo
