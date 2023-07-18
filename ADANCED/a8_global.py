a = 21 #global variable
def fun1():
    global a
    print(a)
    a = 8 #local variable if global keyboard is not used
    print(a)

fun1()
print(a)