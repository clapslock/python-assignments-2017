

def squareAnimation():


    while True:

        frameHeight = int(input("Please enter frame's height: \nRemember: Odd numbers only!\n"))
        frameWidth = int(input("Please enter frame's width:\nRemember: Odd numbers only!\n"))


        if (frameHeight % 2 != 0 and frameWidth % 2 != 0):
            break
    numberOfFrames = min(int(frameWidth/2), int(frameHeight/2))
    frameMiddleRow = int(frameHeight / 2)
    frameMiddleColumn = int(frameWidth / 2)
    numberOfHorizontalXes = 3
    #blank frame
    lineTemplate = "o " * frameWidth
    blankFrame = [lineTemplate] * frameHeight
    firstFrame = blankFrame

    findListCenter(firstFrame, frameHeight, frameWidth)

    completeListOfFrames = []
    completeListOfFrames.append(firstFrame)

    for currentFrame in range(0, numberOfFrames):
        if currentFrame < numberOfFrames:
            loopFrame = blankFrame
            numberofOs = int((frameWidth - numberOfHorizontalXes) / 2 )

            #top, middle and bottom of the square
            loopFrame[numberOfFrames - currentFrame] = "o " * numberofOs + "x " * numberOfHorizontalXes + "o " * numberofOs
            loopFrame[(numberOfFrames + 1) + currentFrame] = "o " * numberofOs + "x " * numberOfHorizontalXes + "o " * numberofOs
            loopFrame[frameMiddleRow] = "o " * numberofOs + "x " + "o " * (frameWidth - (2 * numberofOs + 2)) + "x " + "o " * numberofOs

            numberOfHorizontalXes += 2

            #square's walls
            for frameIndex in range(0, currentFrame):
                loopFrame[frameMiddleRow + frameIndex] = "o " * numberofOs + "x " + "o " * (frameWidth - (2 * numberofOs + 2)) + "x " + "o " * numberofOs
                loopFrame[frameMiddleRow - frameIndex] = "o " * numberofOs + "x " + "o " * (frameWidth - (2 * numberofOs + 2)) + "x " + "o " * numberofOs

            completeListOfFrames.append(loopFrame)
            currentFrame += 1

    printListWithoutBrackets(completeListOfFrames)

def findListCenter(frame, height, width):
    frame[int(height / 2)] = "o " * (int(width / 2)) + "x " + "o " * (int(width / 2))
    return frame

def printListWithoutBrackets(frame):
    for list in frame:

        for line in list:
            tempLine = line
            print("".join(tempLine))
        print ("\n")

squareAnimation()