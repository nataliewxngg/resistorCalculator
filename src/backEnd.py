# not done, i just noticed there's more %s to the fourth band colors, will update fourthBandColors soon 

print("Welcome to Resistor Calculator!\n")
bands = int(input("How many bands of colors are on your resistor? "))    

while bands<3 or bands>6:
    bands = int(input("Invalid input. How many bands of colors are on your resistor? "))

class resistorCalculator:
    def __init__(self, colors,ohm,colorsList,fourthBandColors) -> None:
        self.colors=colors
        self.ohm=ohm
        self.colorsList=colorsList
        self.fourthBandColors=fourthBandColors
        # print(self.colors)
    def threeBands(self):
        for count in range(2):
            index=self.colorsList.index(self.colors[count]) # finds the index of the first color in list

            self.ohm=self.ohm+str(index)
            # print(ohm)
        index=self.colorsList.index(self.colors[2])
        self.ohm=self.ohm+(index*"0")
        print(self.ohm,"ohms within 20%.")

    def fourBands(self):
        for count in range(2):
            index=self.colorsList.index(self.colors[count]) # finds the index of the first color in list

            self.ohm=self.ohm+str(index)
            # print(ohm)
        index=self.colorsList.index(self.colors[2])
        self.ohm=self.ohm+(index*"0")

        print(self.ohm,"ohms within",str(self.fourthBandColors.index(self.colors[3]))+"%.")

    def fiveBands(self):
        for count in range(3):
            index=self.colorsList.index(self.colors[count])

            self.ohm=self.ohm+str(index)
        index=self.colorsList.index(self.colors[3])
        self.ohm=self.ohm+(index*"0")
        
        print(self.ohm,"ohms within",str(self.fourthBandColors.index(self.colors[4]))+"%.")

fst="first"
colors=[]
colorsList=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
fourthBandColors=[0,"brown", "red",3,4,"gold",6,7,8,9,"silver"]
ohm=""

if bands==3:
    for count in range(3):
        colorsInput=str(input("Enter the " + fst + " band color: "))
        while colorsInput not in colorsList:
            colorsInput=str(input("Invalid, Enter the " + fst + " band color: "))
        if colorsInput in colorsList:
            colors.append(colorsInput)
        
        # print(count)
        if count==0:
            fst="second"
        elif count==1:
            fst="third"

    resistor = resistorCalculator(colors,ohm,colorsList,fourthBandColors)
    resistor.threeBands()

elif bands==4:
    for count in range(3):
        colorsInput=str(input("Enter the " +fst+" band color: "))
        while colorsInput not in colorsList:
            colorsInput=str(input("Invalid, Enter the " + fst + " band color: "))
        if colorsInput in colorsList:
            colors.append(colorsInput)
        if count==0:
            fst="second"
        elif count==1:
            fst="third"
    # print(colors)
    colorsInput=str(input("Enter the fourth band color: "))
    while colorsInput not in fourthBandColors:
        colorsInput=str(input("Invalid, Enter the fourth band color: "))
    if colorsInput in fourthBandColors:
        colors.append(colorsInput)

    resistor=resistorCalculator(colors,ohm,colorsList,fourthBandColors)
    resistor.fourBands()

# 5 bands not done
elif bands==5:
    for count in range(4):
        colorsInput=str(input("Enter the "+fst+" band color: "))
        while colorsInput not in colorsList:
            colorsInput=str(input("Invalid, Enter the "+fst+" band color: "))
        if colorsInput in colorsList:
            colors.append(colorsInput)
        if count==0:
            fst="second"
        elif count==1:
            fst="third"
        elif count==2:
            fst="fourth"
    colorsInput=str(input("Enter the fifth band color: "))
    while colorsInput not in fourthBandColors:
        colorsInput=str(input("Invalid, Enter the fifth band color: "))
    if colorsInput in fourthBandColors:
        colors.append(colorsInput)
    
    resistor=resistorCalculator(colors,ohm,colorsList,fourthBandColors)
    resistor.fiveBands()