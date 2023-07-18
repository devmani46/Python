''' Create a class with a class attribute a; create an object 
from it and set a directly using object a=0. Does this change the 
class attribute?'''

class sample:
    a = "asd"

obj = sample()
obj.a = "dev"

print(sample.a)
print(obj.a)

#answer is no