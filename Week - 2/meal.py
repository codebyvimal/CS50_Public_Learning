def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8.0:
        print("Breakfast time")
    if 12 <= time <= 13:
        print("Lunch time")
    if 19 >= time >= 18:
        print(" Dinner time")
    else:
        pass



def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)/60
    return float (x + y)



if __name__ == "__main__":
    main()
