try:
    i=int(input("Enter a number :"))
    c= 1/i
except Exception as e:
    print(e)
finally:
    print("We were successfull")
