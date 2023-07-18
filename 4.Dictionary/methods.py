dict={
    "fast": "in a Qick manner",
    "python" :"programming language",
    "age":[1,2,3],
    "anotherdict":{'python':'Snake'}, #nested dictionary
    1 : 1212
}

print(list(dict.keys())) #prints all word
print(list(dict.values())) #prints all meaning
print(list(dict.items())) #prints all word with meanings
print(dict)


# to add a word with meaning in the dictionary
updatedict={
    "guitar":"musical instrument"
}
dict.update(updatedict)

#to print specific meaning of the word
print(dict)

print(dict.get("python")) #prints given meaning
