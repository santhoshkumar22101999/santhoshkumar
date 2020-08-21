d1=int(input("enter a number"))
d2=int(input("enter another number"))
rem=d1%d2
while(rem!=0):
    d1=d2
    d2=rem
    rem=d1%d2
print(d2)
