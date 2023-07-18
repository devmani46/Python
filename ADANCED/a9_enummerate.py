list1 = [1,4,True,"dev",1.2]

'''
index = 0
for item in list1:
    print(index, item)
    index += 1
'''
# second method

for index, item in enumerate(list1):
    print(index,item)