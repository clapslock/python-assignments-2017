import copy
import time

def squareAnimation():

    while True:

        height = int(input("Please enter frame's height: \nRemember: Odd numbers only!\n"))
        width = int(input("Please enter frame's width:\nRemember: Odd numbers only!\n"))

        if (height % 2 != 0 and width % 2 != 0):
            break
    numberOfFrames = min(int(width/2), int(height/2))
    middleRow = int(height / 2)
    middleColumn = int(width / 2)

    numberOfHorizontalXes = 3
    lineTemplate = "o " * width
    blankFrame = [lineTemplate] * height
    currentFrameIndex = 1

    completeListOfFrames = ([blankFrame] * (numberOfFrames + 1)) #an array filled with blankGrames

    firstFrame = copy.deepcopy(blankFrame)
    firstFrame [int(height / 2)] = "o " * (int(width / 2)) + "x " + "o " * (int(width / 2))

    completeListOfFrames[0] = firstFrame

    for frame in completeListOfFrames:
        if frame == firstFrame:
            continue

        numberOfO = int((width - numberOfHorizontalXes) / 2)
        loopFrameCopy = copy.deepcopy(frame)

        loopFrameCopy[middleRow + currentFrameIndex] = "o " * numberOfO + "x " * numberOfHorizontalXes + "o " * numberOfO
        loopFrameCopy[middleRow - currentFrameIndex] = "o " * numberOfO + "x " * numberOfHorizontalXes + "o " * numberOfO
        loopFrameCopy[middleRow] = "o " * numberOfO + "x " + "o " * (width - (2 * numberOfO + 2)) + "x " + "o " * numberOfO

        for wallIndex in range(1, currentFrameIndex):
            loopFrameCopy[middleRow + wallIndex] = "o " * numberOfO + "x " + "o " * (width - (2 * numberOfO + 2)) + "x " + "o " * numberOfO
            loopFrameCopy[middleRow - wallIndex] = "o " * numberOfO + "x " + "o " * (width - (2 * numberOfO + 2)) + "x " + "o " * numberOfO

        completeListOfFrames[currentFrameIndex] = loopFrameCopy

        numberOfO += 3
        numberOfHorizontalXes += 2
        currentFrameIndex += 1

    revCompleteListOfFrames = copy.deepcopy(completeListOfFrames[::-1])
    revCompleteListOfFrames.pop(0)
    finalList = completeListOfFrames + revCompleteListOfFrames
    printListWithoutBrackets(finalList)

def printListWithoutBrackets(frameOfFrames):

    for frame in frameOfFrames:
        for line in frame:

           print("".join(line))
        time.sleep(0.3)
        print("\n")

squareAnimation()