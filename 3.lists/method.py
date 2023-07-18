l1=[1,32,5,45,7,34]
print(l1)

# asscending
l1.sort()
print("in ascending order",l1)


#decending
l1.reverse()
print("in decending order",l1)


#appends (adds one more string at the end of the list)
l1.append(6)
print("adding 6 in last(appending)",l1)



#insert (adds one more string at the given posotion of the list)
l1.insert(0,99)
print("inserting 99 in 0th posotion",l1)
l1.insert(3,46)
print("inserting 46 in 3rd posotion",l1)



#pop(Removes a string  of the given position)
l1.pop (3)
print("removing 3rd string",l1)

#remove(removes the given string)
l1.remove(7)
# l1.remove(0) #gives error : no 0 in the string
print("removing 7 from string",l1) 

#sum of all elements
print(sum(l1))