import random
s=input("enter your choice..\n1.Rock\n2.Paper\n3.Scissor")
a=["rock","paper","scissor"]
rock=1
paper=2
scissor=3
b=random.choice(a)
print(b)
if(b.rock>b.paper):
    print("rock wins")


