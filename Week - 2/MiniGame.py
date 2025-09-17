import random
print("Welcome to Stone Paper Scissors")

Computer = ["stone","paper","scissors"]
Decision = random.choice(Computer)

user = input("Type your choice ").lower()

print("Computer chooses " + Decision)

if (user == "stone" and Decision == "paper"):
     print("You Lose 😟")
elif(user == "scissors" and Decision == "stone"):
     print("You Lose 😟")
elif(user == "paper" and Decision == "scissors"):
    print("You Lose 😟")
elif user == Decision:
     print("Draw ✋")
elif user != "stone" or user != "paper" or user != "scissors":
     print("Wait, What?🤔")
else:
     print("You Win 🏆")