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
firstBandColor4=secondBandColor4=thirdBandColor4=fourthBandColor4=white
listOfNormalColors=[(0,0,0),(92,64,51),(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(221,160,221),(128,128,128),(255,255,255)]
# black,brown,red,orange,yellow,green,blue,violet,grey,white
listOfMultiplierColors=[(0,0,0),(92,64,51),(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(221,160,221),(128,128,128),(255,255,255),(212,175,55),(192,192,192)]
# black,brown,red,orange,yellow,green,blue,violet,grey,white,gold,silver
listOfToleranceColors=[(92,64,51),(255,0,0),(255,165,0),(255,255,0),(0,255,0),(0,0,255),(221,160,221),(128,128,128),(212,175,55),(192,192,192),(255,255,255)]
# brown,red,orange,yellow,green,blue,violet,grey,gold,silver
dictOfToleranceColors={
    (92,64,51):"1%",
    (255,0,0):"2%",
    (255,165,0):"3%",
    (255,255,0):"4%",
    (0,255,0):"0.5%",
    (0,0,255):"0.25%",
    (221,160,221):"0.1%",
    (128,128,128):"0.05%",
    (212,175,55):"5%",
    (192,192,192):"10%",
    (255,255,255):""
}
# brown,red,orange,yellow,green,blue,violet,gray,gold,silver

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

def calculate3(thirdBandColor3,fourthBandColor3,fifthBandColor3,listOfNormalColors,listOfMultiplierColors,ohm):
    ohm=""
    colors=[thirdBandColor3,fourthBandColor3,fifthBandColor3]

    for count in range(2):
        index=listOfNormalColors.index(colors[count])
        ohm=ohm+str(index)

    index=listOfMultiplierColors.index(colors[2])

    if index>=0 and index<=9:
        ohm=int(ohm)*(10**(index))
    else:
        if index==10:
            ohm=int(ohm)/10
        elif index==11:
            ohm=int(ohm)/100

    global finalOhm
    finalOhm=f"{ohm} ohms 20%"
    print(finalOhm)

def calculate4(firstBandColor4,secondBandColor4,thirdBandColor4,fourthBandColor4,listOfNormalColors,listOfMultiplierColors,ohm):
    ohm=""
    colors=[firstBandColor4,secondBandColor4,thirdBandColor4,fourthBandColor4]

    for count in range(2):
        index=listOfNormalColors.index(colors[count])
        ohm=ohm+str(index)

    index=listOfMultiplierColors.index(colors[2])

    if index>=0 and index<=9:
        ohm=int(ohm)*(10**(index))
    else:
        if index==10:
            ohm=int(ohm)/10
        elif index==11:
            ohm=int(ohm)/100

    tolerance=dictOfToleranceColors.get(fourthBandColor4)

    global finalOhm
    finalOhm=f"{ohm} ohms {tolerance}"
    print(finalOhm)

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
                    calculate3(thirdBandColor3,fourthBandColor3,fifthBandColor3,listOfNormalColors,listOfMultiplierColors,ohm)
                    calculated=True
                elif chosen==4 and mouse[0]>320 and mouse[0]<440 and mouse[1]>320 and mouse[1]<360:
                    calculate4(firstBandColor4,secondBandColor4,thirdBandColor4,fourthBandColor4,listOfNormalColors,listOfMultiplierColors,ohm)
                    calculated=True
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

                        if listOfMultiplierColors.index(fifthBandColor3)==11:
                            fifthBandColor3=listOfMultiplierColors[0]
                        
                        else: fifthBandColor3=listOfMultiplierColors[listOfMultiplierColors.index(fifthBandColor3)+1]       

                elif chosen==4:
                    if selected==1:
                        calculated=False

                        if listOfNormalColors.index(firstBandColor4)==9:
                            firstBandColor4=listOfNormalColors[0]

                        else: firstBandColor4=listOfNormalColors[listOfNormalColors.index(firstBandColor4)+1]

                    elif selected==2:
                        calculated=False

                        if listOfNormalColors.index(secondBandColor4)==9:
                            secondBandColor4=listOfNormalColors[0]

                        else:
                            secondBandColor4=listOfNormalColors[listOfNormalColors.index(secondBandColor4)+1]

                    elif selected==3:
                        calculated=False

                        if listOfMultiplierColors.index(thirdBandColor4)==11:
                            thirdBandColor4=listOfMultiplierColors[0]

                        else: thirdBandColor4=listOfMultiplierColors[listOfMultiplierColors.index(thirdBandColor4)+1]

                    elif selected==4:
                        calculated=False

                        if listOfToleranceColors.index(fourthBandColor4)==10:
                            fourthBandColor4=listOfToleranceColors[0]

                        else: fourthBandColor4=listOfToleranceColors[listOfToleranceColors.index(fourthBandColor4)+1] 

                elif chosen==5:
                    print("dslkfjsd")

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

                        if listOfMultiplierColors.index(fifthBandColor3)==0:
                            fifthBandColor3=listOfMultiplierColors[-1]

                        else: fifthBandColor3=listOfMultiplierColors[listOfMultiplierColors.index(fifthBandColor3)-1]

                elif chosen==4:
                    if selected==1:
                        calculated=False

                        if listOfNormalColors.index(firstBandColor4)==0:
                            firstBandColor4=listOfNormalColors[-1]

                        else: firstBandColor4=listOfNormalColors[listOfNormalColors.index(firstBandColor4)-1]

                    elif selected==2:
                        calculated=False

                        if listOfNormalColors.index(secondBandColor4)==0:
                            secondBandColor4=listOfNormalColors[-1]

                        else: secondBandColor4=listOfNormalColors[listOfNormalColors.index(secondBandColor4)-1]

                    elif selected==3:
                        calculated=False

                        if listOfMultiplierColors.index(thirdBandColor4)==0:
                            thirdBandColor4=listOfMultiplierColors[-1]
                        
                        else:
                            thirdBandColor4=listOfMultiplierColors[listOfMultiplierColors.index(thirdBandColor4)-1]

                    elif selected==4:
                        calculated=False

                        if listOfToleranceColors.index(fourthBandColor4)==0:
                            fourthBandColor4=listOfToleranceColors[-1]

                        else: fourthBandColor4=listOfToleranceColors[listOfToleranceColors.index(fourthBandColor4)-1]
                
                elif chosen==5:
                    print("sdfsdfsdfasdf")

    if windowType == 0: 
        menu(win)

    elif windowType == 1:
        if chosen == 3:
            thirdBand(win,thirdBandColor3,fourthBandColor3,fifthBandColor3,white,calculated,finalOhm,pygame.font.Font("assets/GOUDOSB.TTF",35))

        elif chosen == 4:
            fourthBand(win,firstBandColor4,secondBandColor4,thirdBandColor4,fourthBandColor4,white,calculated,finalOhm,pygame.font.Font("assets/GOUDOSB.TTF",35))

        else:
            fifthBand(win,white)

    pygame.display.update() 
    