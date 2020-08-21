def cmpndintrst(p,t,r):
    amount=p*(pow((1+r/100),t))
    CI=amount-p
    return CI
p=float(input("enter principle"))
r=float(input("enter rate"))
t=int(input("enter time period"))
a=cmpndintrst(p,t,r)
print("compound intrest is",a)
