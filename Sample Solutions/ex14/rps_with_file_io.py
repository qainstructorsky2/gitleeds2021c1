from random import randint
from time import sleep
from os.path import isfile

if isfile("scores.txt"):
    with open('scores.txt', 'r') as f:
        f.read()  # writes to data as list, not string
else:
    data = {'wins': 0, 'loses': 0, 'draws': 0}
    with open("scores.txt", "w+") as f:
        f.write("{'wins': 0, 'loses': 0, 'draws': 0}")


def playgame():
    while True:
        global player
        player = input("Choose Rock, Paper or Scissors:")
        if player == "rock" or player == "r":
            print("You have chosen Rock")
            player = 0
            break
        elif player == "paper" or player == "p":
            print("You have chosen Paper")
            player = 1
            break
        elif player == "scissors" or player == "s":
            print("You have chosen Scissors")
            player = 2
            break
        else:
            print("Error: Incorrect Input")

    sleep(1)

    computer = randint(0, 2)
    if computer == 0:
        print("Computer has chosen Rock")
    elif computer == 1:
        print("Computer has chosen Paper")
    else:
        print("Computer has chosen Scissors")

    if player == computer:
        print("It's a draw!")
        data["draws"] += 1
    elif player == 0 and computer == 1:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 0 and computer == 2:
        print("You have won!")
        data["wins"] += 1
    elif player == 1 and computer == 0:
        print("You have won!")
        data["wins"] += 1
    elif player == 1 and computer == 2:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 2 and computer == 0:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 2 and computer == 1:
        print("You have won!")
        data["wins"] += 1
    with open("scores.txt", "w+") as f:
        f.write(str(data))

    print('''
=========================
You have %d total wins
You have %d total loses
You have %d total draws

You have played %d times
=========================
''' % (data["wins"], data["loses"], data["draws"],
       data["wins"] + data["loses"] + data["draws"]))


def plagain():
    while True:
        again = input('''
"Type 'Yes' or 'No' if you either want to play again or close the program or
'Reset' to reset your score and close the program:''').lower()
        if again == "yes" or again == "y":
           playgame()
        elif again == "no" or again == "n":
            break
        elif again == "reset" or again == "r":
            with open("scores.txt", "w+") as f:
                f.write("{'wins': 0, 'loses': 0, 'draws': 0}")
            print("Score Reset Successfully!")
            sleep(1)
            break
        else:
            print("Error:Incorrect Input")


#if __name__ == "__main__":
print("'Rock, Paper, Scissors'")

playgame()
