

triangle_side = input("Lenght of the side of your triangle: ")

if triangle_side.isdigit():
    float(triangle_side)
else:
    while triangle_side.isdigit() != True:
        triangle_side = input("Lenght of the side of your triangle: ")

triangle_height = input("Height of the trinagle: ")

if triangle_height.isdigit():
    float(triangle_height)
else:
    while triangle_height.isdigit() != True:
        triangle_height = input("Height of the trinagle: ")

triangle_field_area = float(triangle_side) * float(triangle_height) * 0.5

print("Your trinagle's area field equals: ", triangle_field_area)



