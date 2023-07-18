""" a list contains the multiplication of 7. WAP to convert 
it to a vertcal string of same numbers
(7
 14
 .
 .
 .)
"""


l = [str(i*7) for i in range(1,11)]
print(l)

verticle= "\n".join(l)
print(verticle)