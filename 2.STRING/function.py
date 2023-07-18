b="hi \nhello world \tgood morning \ngood day"

# string functions
print(len(b)) #length of string
print(b.endswith("day")) #check if string ends with given word
c=b.count("h") #counts specific word
print(c)           # print(b.count("h"))  
print(b.capitalize()) #capitalizes fisrt word
print(b.find("world")) #finds the posotion of the word
print(b.replace("good","bad")) #replaces the words
