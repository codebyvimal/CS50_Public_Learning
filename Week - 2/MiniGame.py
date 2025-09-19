import random
def main():
     print("Welcome to Stone Paper Scissors")

     Computer = ["stone","paper","scissors"]
     Decision = random.choice(Computer)

     user = input("Type your choice ").lower()

     print("Computer chooses " + Decision)

     if (user == "stone" and Decision == "paper"):
          lose()
     elif(user == "scissors" and Decision == "stone"):
           lose()
     elif(user == "paper" and Decision == "scissors"):
          lose()
     elif user == Decision:
          draw()
     elif user != "stone" or user != "paper" or user != "scissors":
          print("Wait, What?🤔")
     else:
          win() 

def lose():
     print("You Lose 😟")
def win():
     print("You Win 🏆")
def draw():
     print("Draw ✋")
main()