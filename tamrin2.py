import random
computerscore=0
userscore=0
while computerscore<5 and userscore<5 :
    x =random.randint(1,3)
    if x==1:
        computerchoice="rock"
    elif x==2:
        computerchoice="paper"
    elif x==3:
        computerchoice="scissor"
    userchoice=input("rock or scissor or paper:")
    print("computerchoice",computerchoice)
    print("userchoice",userchoice)
    if computerchoice=="rock" and userchoice=="paper":
        userscore=userscore+1
    elif computerchoice=="rock" and userchoice=="scissor":
        computerscore=computerscore+1
    elif computerchoice=="rock" and userchoice=="rock":
        print("no score")
    elif computerchoice=="paper" and userchoice=="rock":
        computerscore=computerscore+1
    elif computerchoice=="paper" and userchoice=="scissor":
        userscore=userscore+1
    elif computerchoice=="paper" and userchoice=="paper":
        print("noscore")
    elif computerchoice=="scissor" and userchoice=="rock":
        userscore=userscore+1
    elif computerchoice=="scissor" and userchoice=="paper":
        computerscore=computerscore+1
    elif computerchoice=="scissor" and userchoice=="scissor":
        print("noscore")
    
print("computerscore",computerscore,end=" ")
print("userscore",userscore,end=" ")
