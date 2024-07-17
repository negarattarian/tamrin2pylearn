a=int(input("input a number for fibonanchi series:"))
b=1
c=1
print(b,end=" ")
print(c,end=" ")
count=2
while count<a:
    d=b+c
    print(d,end=" ")
    b=c
    c=d
    count+=1