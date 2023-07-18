""" WAP a program to find the maxiumum of the numbers in a 
list using the reduce function"""

from functools import reduce
l = [1,4,5,2,8,0,19]
a= reduce(max, l)
print(a)