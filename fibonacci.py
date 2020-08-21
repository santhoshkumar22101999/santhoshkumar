def fibo(n):
    a=0
    b=1
    if(n<0):
        print("invalid number")
    elif(n==0):
        print("A")
    elif(n==1):
        print("b")
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b

print(fibo(int(input("enter a number"))))
