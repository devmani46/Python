l='''dear <|name|>,
you are selected!

Date: <|date|>
'''
name=input("enter your name:\n")
date=input("enter date:\n")
l=l.replace("<|name|>",name)
l=l.replace("<|date|>",date)
print(l)