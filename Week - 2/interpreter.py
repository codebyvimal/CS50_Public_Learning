input = input("Expression: ")

x,y,z =input.split(" ")

if y == ("+"):
    print(float(x) + float(z))
elif y == ("-"):
    print(float(x) - float(z))
elif y == ("/"):
    print(float(x)/float(z))
elif y == ("*"):
    print(float(x) * float(z))
