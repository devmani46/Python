#strip removes the unnecessary spaces
def remove_and_split(string, word):
    newstr=string.replace(word,"") #removing the word #replacing with blank
    return newstr.strip()

g="    hi hello   hehe  goodmorning user"
n = remove_and_split(g, "hello")
print(n)