n=int(input("enter a number"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev+dig**3
    n=n//10
if(temp==rev):
    print("Armstrong number")
else:
    print("not an Armstrong number")
