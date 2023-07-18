a=int(input("enter marks in english :"))
b=int(input("enter marks in computer :"))
c=int(input("enter marks in science :"))
d=(a+b+c)/3

if(a<33 or b<33 or c<33):
    print("You are failed")


elif(d<40):
    print("you are failed")

else:
    print("you are passed")