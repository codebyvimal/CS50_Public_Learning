def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) == True and first2(s) == True and alphanum(s) == True and notzero(s) == True and is_correct(s) == True:
        return True
    else:
        return False


def length(s): # to check the length
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False
def first2(s): #to check if first two are alphabets
    temp = s[0:2]
    if temp.isalpha():
        return True
    else:
        return False
def alphanum(s): # to check there are no spaces or spaces
    if s.isalnum():
        return True
    else:
        return False
def notzero(s):
    if isitzero(s) == True:
        return False
    else:
        return True
# the functions thenumber, isitzero and
def thenumber(s):
    for i in s:
        if i.isdigit():
            return i
    return "1"
def isitzero(s):
    if int(thenumber(s)) == 0:
        return True
    else:
        return False

def is_correct(s):
    seen_a_num = False
    for i in s:
        if i.isdigit():
            seen_a_num = True

        if i.isalpha() and seen_a_num == True:
            return False
    return True

main()
