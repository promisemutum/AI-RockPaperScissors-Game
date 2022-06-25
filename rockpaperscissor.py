#a game between two computers
#human vs computer will be added soon
import random
redcount = 0
bluecount = 0
turns = int(input("Enter the number of rounds: "))
List = ['rock', 'paper', 'scissors']
for i in range(0, turns):
    red = random.choice(List)
    random.shuffle(List)
    blue = random.choice(List)
    random.shuffle(List)
    if red == "rock" and blue == "paper":
        print("Blue Wins!")
        bluecount += 1
    elif red == "rock" and blue == "scissors":
        print("Red Wins!")
        redcount += 1
    elif red == "paper" and blue == "scissors":
        print("Blue Wins!")
        bluecount += 1
    elif red == "paper" and blue == "rock":
        print("Red Wins!")
        redcount += 1
    elif red == "scissors" and blue == "paper":
        print("Red Wins!")
        redcount += 1
    elif red == "scissors" and blue == "rock":
        print("Blue Wins!")
        bluecount += 1
    elif red == blue:
        print("Draw!!!")
print("")
if redcount < bluecount:
    print("Blue Wins with " + str(bluecount) + "points")
elif redcount > bluecount:
    print("Red Wins with " + str(redcount )+ "points")
else:
    print("Boths teams have a draw!")
