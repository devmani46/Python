# to read n number of lines
f = open('sample.txt')
# reads frst lines
data = f.readline()
print(data)

# reads second line 
data = f.readline()
print(data)

# and son on 
data = f.readline()
print(data)

f.close()
