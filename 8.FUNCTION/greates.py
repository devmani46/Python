def great(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    if(num2>num1 and num2>num3):
        return num2
    else:
        return num3

num1=int(input("Enter first  number : "))
num2=int(input("Enter second  number : "))
num3=int(input("Enter third  number : "))
m=great(num1,num2,num3)
print("the greatest num is ", str(m))