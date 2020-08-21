def simpleintrst(p,t,r):
    ans=(p*t*r)/100
    return ans
p=float(input("enter principle"))
r=float(input("enter rate"))
t=int(input("enter time period"))
a=simpleintrst(p,t,r)
print("simple intetrest is",a)
