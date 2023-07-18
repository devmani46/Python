#relationalsa operators #<,>,==,<=,>=
a=int(input("enter your age:\n"))
if(a>=18):
    print("you can vote")
else:
    print("you can't vote")

#logical operators #and, or , not
b=int(input("enter your age:\n"))
if(b>=18 and b<=40):  #we can use and, or , not 
    print("you are adult")
else:
    print("you aren't adult")