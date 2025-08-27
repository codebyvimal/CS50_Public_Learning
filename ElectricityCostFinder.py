
def units():
    return float(input("How much units were spent this month? "))

def cost_per_unit():
    return float(input("What's the cost per Unit in your area? ").replace("₹",""))

def fixed_charges():
    return float(input("Mention the fixed charges, if any.").replace("₹",""))

def total():
    Total_cost = str(units() * cost_per_unit() + fixed_charges())
    return Total_cost

def main():
    print(" ⚡️Welcome to Electricity Calculator ⚡️")
    print("₹" + total())


main()
