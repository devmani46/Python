# to create empty set
d=set()
print(d)
print(type(d))

#methods
# adding values to empty set
d.add(5)
d.add(1)
d.add((1,2,3))
# d.add{1,2} # we can add tuple()in sets but not list{} nor dictionary{1:2}
print(d)
# to print the length of the set
print(len(d))

#to remove a character from the set
d.remove(5) 
print(d)


#to remove random value
a={1,2,3,(4,5,6)}
print(a)
a.pop()
print(a)

# to empty the set
i={2,4,123,4345,123}
print(i.clear())


# to print the unswion of the set
e={1,2,3,6}
print(e.union({6,7,8,}))

# to print the intersection of the set
f={1,2,3,5,7,8}
print(f.intersection({1,5,6,7}))
