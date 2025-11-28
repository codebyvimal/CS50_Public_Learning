import random
while True:
    try:
        n = int(input("Level: "))
        if n >= 0:
            break
    except ValueError:
        pass

choice = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))

        if guess < 1:
            continue

        if guess == choice :
            print("Just Right!")
            break
        elif guess > choice:
            print("Too large!")
        elif guess < choice :
            print("Too small!")
    except ValueError:
        pass
