#Getting correct input
def get_input():
    while True:
        try:
            x = input("Fraction: ").split("/")
            if int(x[0]) <= int(x[1]) and int(x[0]) >= 0 and int (x[1]) >= 0:
                return round(int(x[0]) * 100 / int(x[1]))
        except ValueError or ZeroDivisionError:
            pass
q = get_input()
if q <= 1:
    print("E")
elif q >= 99:
    print("F")
else:
    print(f"{q}%")
