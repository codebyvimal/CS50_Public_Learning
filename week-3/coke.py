paid = 0
total = 50
pending = 0
print("Amount Due: 50")
while paid <= 50:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        paid = paid + coin
    if total > paid:
        pending = total - paid
        print("Amount Due:",pending)
    if paid > total:
        give = paid - total
        print("Change Owed:", give)
    if paid == total:
        print("Change Owed: 0")
        break
