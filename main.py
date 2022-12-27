# from src.backEnd import resistorCalculator 
import pygame
from src.displays import*

# initiation
pygame.init() # initializes all pygame modules
win=pygame.display.set_mode((800,400))
pygame.display.set_caption('Resistor Calculator'.upper())

#vars
running=True
selected=0
white=(255,255,255)
windowType = 0 # 0 means the main menu is open, 1 means selecting colour menu is open
calculated=False
ohm=""
finalOhm=""
thirdBandColor3=fourthBandColor3=fifthBandColor3=white
listOfNormalColors=[(255,255,255),(0,0,0),(92,64,51),(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(221,160,221),(128,128,128)]
# black,brown,red,orange,yellow,green,blue,violet,grey,white

# functions needed in pygame.event.get loop
def chooseBandsNum() : # check if one of the squares is clicked on
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

def returnToMenu(): #check if a colour is chosen, or if the cancel button is pressed
    mouse=pygame.mouse.get_pos()
    if mouse[0]>20 and mouse[0]<170 and mouse[1]>20 and mouse[1]<60: 
        global windowType
        windowType = 0

def checkSelectedBand(chosen):
    mouse=pygame.mouse.get_pos()
    global selected

    if chosen==3:
        if mouse[0]>200 and mouse[0]<330 and mouse[1]>90 and mouse[1]<310:
            selected=1
        elif mouse[0]>325 and mouse[0]<435 and mouse[1]>90 and mouse[1]<310:
            selected=2
        elif mouse[0]>450 and mouse[0]<560 and mouse[1]>90 and mouse[1]<310:
            selected=3
        else:
            selected=0
    
    elif chosen==4:
        if mouse[0]>145 and mouse[0]<255 and mouse[1]>90 and mouse[1]<310:
            selected=1
        elif mouse[0]>270 and mouse[0]<380 and mouse[1]>90 and mouse[1]<310:
            selected=2
        elif mouse[0]>395 and mouse[0]<505 and mouse[1]>90 and mouse[1]<310:
            selected=3
        elif mouse[0]>520 and mouse[0]<630 and mouse[1]>90 and mouse[1]<310:
            selected=4
        else: 
            selected=0
    
    elif chosen==5:
        if mouse[0]>90 and mouse[0]<200 and mouse[1]>90 and mouse[1]<310:
            selected=1
        elif mouse[0]>215 and mouse[0]<325 and mouse[1]>90 and mouse[1]<310:
            selected=2
        elif mouse[0]>340 and mouse[0]<505 and mouse[1]>90 and mouse[1]<310:
            selected=3
        elif mouse[0]>465 and mouse[0]<630 and mouse[1]>90 and mouse[1]<310:
            selected=4
        elif mouse[0]>590 and mouse[0]<720 and mouse[1]>90 and mouse[1]<310:
            selected=5
        else:
            selected=0

    print(selected)

def calculate3(thirdBandColor3,fourthBandColor3,fifthBandColor3,listOfNormalColors,ohm):
    ohm=""
    colors=[thirdBandColor3,fourthBandColor3,fifthBandColor3]

    for count in range(2):
        index=listOfNormalColors.index(colors[count])-1 
    
        ohm=ohm+str(index)

    index=listOfNormalColors.index(colors[2])-1
    ohm=ohm+(index*"0")

    global finalOhm
    finalOhm=f"{ohm}ohms 20%"
    print(finalOhm)

def calculate4():
    mouse=pygame.mouse.get_pos()
    if mouse[0]>320 and mouse[0]<440 and mouse[1]>320 and mouse[1]<360:
        print("4 bands must be calculated.")

def calculate5():
    mouse=pygame.mouse.get_pos()
    if mouse[0]>320 and mouse[0]<440 and mouse[1]>320 and mouse[1]<360:
        print("5 bands must be calculated.")

# main program
while running:

    for event in pygame.event.get(): 
        
        if event.type==pygame.QUIT: 
            running=False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if windowType == 0: # if in menu, check which 'bands' button chosen
                chooseBandsNum()
            
            elif windowType == 1: # if in 'bands' page, check if 'return to menu' button chosen
                returnToMenu()
                checkSelectedBand(chosen)

                mouse=pygame.mouse.get_pos()

                if chosen==3 and mouse[0]>320 and mouse[0]<440 and mouse[1]>320 and mouse[1]<360 and calculated==False:
                    calculate3(thirdBandColor3,fourthBandColor3,fifthBandColor3,listOfNormalColors,ohm)
                    calculated=True
                elif chosen==4:
                    calculate4()
                elif chosen==5:
                    calculate5()
                
        if event.type==pygame.KEYDOWN and windowType==1:
            
            if event.key==pygame.K_RIGHT:
                if chosen==3:
                    if selected==1:
                        calculated=False

                        if listOfNormalColors.index(thirdBandColor3)==9:
                            thirdBandColor3=listOfNormalColors[0]

                        else: thirdBandColor3=listOfNormalColors[listOfNormalColors.index(thirdBandColor3)+1]

                    elif selected==2:
                        calculated=False
                        
                        if listOfNormalColors.index(fourthBandColor3)==9:
                            fourthBandColor3=listOfNormalColors[0]

                        else: fourthBandColor3=listOfNormalColors[listOfNormalColors.index(fourthBandColor3)+1]
                    
                    elif selected==3:
                        calculated=False

                        if listOfNormalColors.index(fifthBandColor3)==9:
                            fifthBandColor3=listOfNormalColors[0]
                        
                        fifthBandColor3=listOfNormalColors[listOfNormalColors.index(fifthBandColor3)+1]
            
            elif event.key==pygame.K_LEFT:
                if chosen==3:
                    if selected==1:
                        calculated=False
                        
                        if listOfNormalColors.index(thirdBandColor3)==0:
                            thirdBandColor3=listOfNormalColors[-1]
                            
                        else: thirdBandColor3=listOfNormalColors[listOfNormalColors.index(thirdBandColor3)-1]

                    elif selected==2:
                        calculated=False

                        if listOfNormalColors.index(fourthBandColor3)==0:
                            fourthBandColor3=listOfNormalColors[-1]
                        
                        else: fourthBandColor3=listOfNormalColors[listOfNormalColors.index(fourthBandColor3)-1]

                    elif selected==3:
                        calculated=False

                        if listOfNormalColors.index(fifthBandColor3)==0:
                            fifthBandColor3=listOfNormalColors[-1]

                        else: fifthBandColor3=listOfNormalColors[listOfNormalColors.index(fifthBandColor3)-1]
                    
    if windowType == 0: 
        menu(win)

    elif windowType == 1:
        if chosen == 3:
            thirdBand(win,thirdBandColor3,fourthBandColor3,fifthBandColor3,white,calculated,finalOhm,pygame.font.Font("assets/GOUDOSB.TTF",35))

        elif chosen == 4:
            fourthBand(win,white)

        else:
            fifthBand(win,white)

    pygame.display.update() 
    