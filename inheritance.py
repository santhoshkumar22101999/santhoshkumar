class Addition:
    def summation(self,a,b):
        print(a+b)
class Subtraction(Addition):
    def sub(self,a,b):
        print(a-b)
class Multiplication(Subtraction):
    def multiply(self,a,b):
        print(a*b)
class Division(Multiplication):
    def divide(self,a,b):
        print(a/b)
a=int(input("enter first number"))
b=int(input("enter another number"))
d=Division()
d.summation(a,b)
d.sub(a,b)
d.multiply(a,b)
d.divide(a,b)
