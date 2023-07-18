"""" WAP to filter a list of numbers which are divisible by 5"""


l= [1,2,4,5,15,25,42,23,10,22,40]

a= filter(lambda a : a%5==0, l)
print(list(a))