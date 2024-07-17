import random
dice_states=[1,2,3,4,5,6]
print("print roll the dice up")
result=random.choice(dice_states)
print("the dice is",":",result)
if result==6:
    print("you have a bonus")
    result=random.choice(dice_states)
    print("newresult:",result)