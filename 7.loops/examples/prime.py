a=int(input("enter a number: "))
    
for i in range(2,a):
    if(a%i==0):
        print("this number is composite")
        break
    else:
        print("this number is  prime")
        break

