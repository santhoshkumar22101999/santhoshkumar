a=list(input("enter a name"))
vowels=['a','e','i','o','u','A','E','I','O','U']
v=[]
cons=[]
for i in range(0,len(a)):
    if a[i] in vowels:
        v.append(a[i])
    else:
        cons.append(a[i])
print("vowels are",v)
print("consonants are",cons)
