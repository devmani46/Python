'''Write a program to open 3 files b1.txt
b2.txt and b3.txt. if any of these files are 
not present, a message without exiting the porgram
must be printing the same.'''

def readFile(filename):
    try:
        with open(filename, "r")as f:
            print(f.read())

    except FileNotFoundError:
        print(f"File {filename} is not found")
readFile("b1.txt")
readFile("b2.txt")
readFile("b3.txt")
