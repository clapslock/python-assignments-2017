
def squareAnimation():

    while True:

        frameHeight = int(input("Please enter frame's height: \nRemember: Odd numbers only!\n"))
        frameWidth = int(input("Please enter frame's width:\nRemember: Odd numbers only!\n"))

        if (frameHeight % 2 != 0 and frameWidth % 2 != 0):
            break

    frameTemplate = [["o"] * frameWidth]*frameHeight

    for outerListElement in range(0, len(frameTemplate)-1):
        for innerListElement in range(0, len(frameTemplate[outerListElement])-1):
            if outerListElement == int(frameHeight / 2) and innerListElement == int(frameWidth / 2):
                frameTemplate[outerListElement] = "o " * int(frameWidth / 2) + "x "

    for object in range(0, len(frameTemplate)):
        tempLine = frameTemplate[object]
        print(" ".join(tempLine))


def squareAnimation2():

    while True:

        frameHeight = int(input("Please enter frame's height: \nRemember: Odd numbers only!\n"))
        frameWidth = int(input("Please enter frame's width:\nRemember: Odd numbers only!\n"))

        if (frameHeight % 2 != 0 and frameWidth % 2 != 0):
            break

    lineTemplate = "o " * frameWidth
    frameTemplate = [lineTemplate] * frameHeight

    findListCenter(frameTemplate, frameHeight, frameWidth)

    for object in range(0, len(frameTemplate)):
        tempLine = frameTemplate[object]
        print("".join(tempLine))

def findListCenter(frame, height, width):
    frame[int(height / 2)] = "o " * (int(width / 2)) + "x " + "o " * (int(width / 2))

squareAnimation2()