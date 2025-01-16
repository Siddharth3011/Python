'''
-1 for rock
1 for paper
0 for scissor

'''

import random
import os

if os.path.exists("score.txt"):
    with open("score.txt", "r") as f:
        try:
            n = int(f.read())  # Read the current score
        except ValueError:
            n = 0  # Initialize to 0 if the file is empty or invalid
else:
    n = 0 

computer = random.choice([-1,0,1])
youstr = input("Enter your choice[paper(p), rock(r), scissor(s)]: ")
youDict = {"r": -1, "p": 1, "s":0}
you = youDict[youstr]
reverseDict = {-1: "rock", 1: "paper", 0: "scissor"}

print(f"you choose: {reverseDict[you]}")
print(f"computer choose: {reverseDict[computer]}")

if(computer == -1 and you == 1):
    print("You win!")
    n +=1
    with open("score.txt","w") as f:
        f.write(str(n))

elif(computer == -1 and you == 0):
    print("you lose!")

elif(computer == 1 and you == -1):
    print("you lose!")

elif(computer == 1 and you == 0):
    print("you win!")
    n +=1
    with open("score.txt","w") as f:
        f.write(str(n))

elif(computer == 0 and you == -1):
    print("you win!")
    n +=1
    with open("score.txt","w") as f:
        f.write(str(n))

elif(computer == 0 and you == 1):
    print("you lose!")

else:
    print("draw")
