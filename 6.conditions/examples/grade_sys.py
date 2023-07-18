marks=int(input("enter your marks : "))

if(marks>=90):
    grades="A+"
elif(marks>=80):
    grades="A"
elif(marks>=70):
    grades="B+"
elif(marks>=60):
    grades="B"
elif(marks>=50):
    grades="C+"
elif(marks>=40):
    grades="C"
else:
    grades="D"

print("your grade is : " , grades)
   