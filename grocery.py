grocery = {}
while True:
    try:
        x = input().upper()
        if x in grocery: grocery[x] = grocery[x] + 1
        else: grocery[x] = 1
    except EOFError: break
for x in sorted(grocery): print(grocery[x],x)


