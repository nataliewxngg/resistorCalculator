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
def menu():
    win.fill((214,206,195))
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))

    font=pygame.font.Font("assets/GOUDOSB.TTF",60)

    resistorText=font.render("RESISTOR",True,white)
    resistorTextRect=resistorText.get_rect()
    resistorTextRect.left=300
    resistorTextRect.top=50
    win.blit(resistorText,resistorTextRect)

    calculatorText=font.render("CALCULATOR",True,white)
    calculatorTextRect=calculatorText.get_rect()
    calculatorTextRect.left=340
    calculatorTextRect.top=100
    win.blit(calculatorText,calculatorTextRect)

    snowmanImg=pygame.image.load("assets/snowman.png")
    win.blit(snowmanImg,(40,0))

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  

    menu()
    pygame.display.update()
    
