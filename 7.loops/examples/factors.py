n=int(input("enter a number: "))

print("the factors of this number are :")
f=0
for i in range (1,n+1):
    f=n%i
    if(f==0):
        print(i) 