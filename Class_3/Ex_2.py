
def squareAnimation():


    while True:

        frameHeight = int(input("Please enter frame's height: \nRemember: Odd numbers only!\n"))
        frameWidth = int(input("Please enter frame's width:\nRemember: Odd numbers only!\n"))


        if (frameHeight % 2 != 0 and frameWidth % 2 != 0):
            break
    numberOfFrames = min(int(frameWidth/2), int(frameHeight/2))

    lineTemplate = "o " * frameWidth
    #frame filled with "o" only
    blankFrame = [lineTemplate] * frameHeight

    #frame with x in center
    frameTemplate = blankFrame
    findListCenter(frameTemplate, frameHeight, frameWidth)
    printListWithoutBrackets(frameTemplate)

    for frameNumber in range(0, numberOfFrames):
        currentFrame = blankFrame

        




def findListCenter(frame, height, width):
    frame[int(height / 2)] = "o " * (int(width / 2)) + "x " + "o " * (int(width / 2))

def printListWithoutBrackets(frame):
    for object in range(0, len(frame)):
        tempLine = frame[object]
        print("".join(tempLine))

squareAnimation()