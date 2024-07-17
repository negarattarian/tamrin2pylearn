grade=[]
while(True):
    grade_input=(input("get scores:"))
    
    if(grade_input=="exit"):
        break
    else:
     int_grade_input=int(grade_input)
     grade.append(int_grade_input) 
    average=sum(grade)/len(grade)
    print("average grde is",average)  