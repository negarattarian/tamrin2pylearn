import random
computernumber=random.randint(10,50)
num_guess=0
for i in range(10):

    usernumber=int(input("guess a number"))
    num_guess+=1

    if computernumber==usernumber:
        print("yooooooooooooooooouuuuuuuuuuuu win✨")
        break
    elif computernumber>usernumber:
        print("go up❤")
    elif computernumber<usernumber:
        print("go down💕")
        
print("number of num guess ",num_guess)