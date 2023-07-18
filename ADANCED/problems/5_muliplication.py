"""Store the multiplication tables generated in
problem  in a file named tables.txt"""

num = int(input("Enter a number : "))

tables = [num * i for i in range(1,11)]
print(tables)
with open("tables.txt","a" ) as f:
    f.write(str(tables))
    f.write("\n")
