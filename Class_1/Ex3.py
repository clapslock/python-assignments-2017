import random

randomInt = random.randrange(0, 10)
randomInt = randomInt

user_guessed_number = input("Take a guess! ")
while True:
    if user_guessed_number.isdigit() == True:
        user_guessed_number = int(user_guessed_number)
        if (user_guessed_number == randomInt):
            print("Congratulations!")
            exit()
        elif user_guessed_number < randomInt:
            print("Lil bit bigger!")
            user_guessed_number = input("Take a guess! ")
            continue
        elif user_guessed_number > randomInt:
            print("Too much!")
            user_guessed_number = input("Take a guess! ")
            continue
    elif user_guessed_number.isdigit() != True:
        print("Numbers only!")
        user_guessed_number = input("Take a guess! ")



