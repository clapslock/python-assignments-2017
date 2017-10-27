
import  math

sideA = input("First side: ")

if sideA.isdigit():
    float(sideA)
else:
    while sideA.isdigit() != True:
        sideA = input("First side: ")

sideB = input("Secondirst side: ")

if sideB.isdigit():
    float(sideB)
else:
    while sideB.isdigit() != True:
        sideB = input("Second side: ")

sideC = input("Third side: ")

if sideC.isdigit():
    float(sideC)
else:
    while sideC.isdigit() != True:
        sideC = input("Third side: ")

sideA = float(sideA)
sideB = float(sideB)
sideC = float(sideC)

p = (float(sideA) + float(sideB) + float(sideC)) * float(0.5)

result = math.sqrt(float(p * (p - sideA) * (p - sideB) * (p - sideC)))

print("Triangle's area = ", result)
