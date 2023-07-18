 #with statement helps to open and close the file automatically 
with open('another.txt','r') as f:
    a=f.read()
with open('another.txt','w') as f:
    a=f.write("me")
print(a)