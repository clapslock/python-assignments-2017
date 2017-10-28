from random import randint
import time
import os

def springRain():

    #user input
    selectedWidth = int(input("Please enter frame's width: \n"))
    selectedHeight = int(input("Please enter frame's height: \n"))

    #create a frame template filled with "o"s
    completeFrame = [["o"] * selectedWidth] * selectedHeight

    numberOfIterations = 1

    while True:
        #interate over rows in a frame
        for yPosition in range(0, selectedHeight):

            x = 0
            while (x <= yPosition):

                randomDropPosition = randint(0, selectedWidth)
                temporaryLineTemplate = ["o"] * selectedWidth
                temporaryLineTemplate[randomDropPosition - 1] = "x"

                #add a new frame on the first place of the completeFrame list
                completeFrame.insert(0, temporaryLineTemplate)

                #print every object of completeFrame in a for loop
                for object in range(0, len(completeFrame)):
                    tempLine = completeFrame[object]
                    print(" ".join(tempLine))

                time.sleep(0.3)

                #"clear" the console by printing multiple \n
                print('\n' * 80)

                #pop the completeFrame's last opbject
                if (len(completeFrame) > selectedHeight):
                    completeFrame.pop()

                #add +1 to the total number of completed lines 
                x += 1

springRain()
