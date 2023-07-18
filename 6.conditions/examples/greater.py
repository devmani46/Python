a=int(input("enter first number:\n"))
b=int(input("enter second number:\n"))
c=int(input("enter third number:\n"))
d=int(input("enter fourth number:\n"))
if(a>b and a>c and a>d):
    print(str(a) +" is the greatest number")

if(b<a and b<c and b<d):
    print(str(b) +" is the greatest number")

if(c>a and c>b and c>d):
    print(str(c) +" is the greatest number")

else:
    print(str(d) +" is the greatest number")