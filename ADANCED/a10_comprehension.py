a = [1,2,3,4,5,11,12,14,13,15,21,22,23,24]
'''
b = []
for item in a:
    if item %2 == 0 :
        b.append(item)

print(b)
'''
#next method
b= [i for i in a if i%2==0]
print(b)
