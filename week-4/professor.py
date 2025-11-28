import random
#Messiest code i ever made

def main():
    level = get_level()
    finalScore = quiz(level)
    print(f"Score: {finalScore}")

# --------------------------------------------
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                level = n
                return level
            else:
                raise ValueError
        except ValueError:
            pass
# ----------------------------------------
def generate_integer(level):
    if level == 1:
        a = 0
        b = 9
    elif level == 2:
        a = 10
        b = 99
    elif level == 3:
        a = 100
        b = 999
    num = random.randint(a,b)
    return num
# -----------------------------------------------
def quiz(level):
     Score = 10
     for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        solved = False
        while solved == False:
            try:
                z = int(input(f"{x} + {y} = "))
                if x + y == z:
                    solved = True
                if x + y != z:
                    raise ValueError
            except ValueError:
                    print("EEE")
                    o = 0
                    for i in range(2):
                        o = o + 1
                        try:
                            z = int(input(f"{x} + {y} = "))
                            if x + y == z:
                                solved = True
                                break
                            elif x + y != z:
                                raise ValueError
                        except ValueError:
                            print("EEE")
                    if o == 2:
                        print(f"{x} + {y} = {x+y}")
                        Score = Score - 1
                        break
     return Score
if __name__ == "__main__":
    main()
