from typing import Text


a=input("enter your text :")
spam=False

if("subscribe me" in a):
    spam = True
elif("like my video" in a):
    spam = True
elif("comment below" in a):
    spam = True
elif("open this link" in a):
    spam = True

else:
    spam=False

if(spam):
    print("this text is a spam")
else:
    print("this text is not spam")
