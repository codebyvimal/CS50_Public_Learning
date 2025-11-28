x = input("Greetings: ")
x = x.lower().strip()
if x == "hello" or x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")
