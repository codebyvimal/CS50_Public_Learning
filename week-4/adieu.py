import inflect

p = inflect.engine()
names = []

x = True
while x == True:
    try:
        b = input("Name: ")
        names.append(b)
    except EOFError:
         print()
         x = False

print(f"Adieu, adieu, to {p.join(names)}")



