try:
    a = int(input("enter a number : "))
    c = 1/a
    print(c)
#except Exception as e:
    #print("Exception1 occured")
    #print(e)

except ValueError as e:
    print("Exception2 occured")

except ZeroDivisionError as e:
    print("Dont divide by zero")

print("Thanks for using this code")