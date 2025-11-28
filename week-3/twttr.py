word = input("Input: ")
output = ""
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        output = output + ""
    else:
        output = output + i
print("Output:", output)

