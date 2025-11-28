camelcase = input("camelCase: ")
snakecase = ""
for i in camelcase:
    if i.isupper():
        snakecase = snakecase + "_" + i.lower()
    else:
        snakecase = snakecase + i
print(snakecase)
