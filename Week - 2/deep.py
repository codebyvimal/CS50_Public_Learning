x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

x = x.strip().lower().replace("-"," ")

if x == "forty two" or x == "42":
    print("Yes")
else:
    print("No")
