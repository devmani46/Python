'''
def factorial_ier(n):
    p=1
    for i in range(n):
        p=p*(i+1)
    return p
a=int(input("enter a number: "))
f=factorial_ier(a)
print(f)
'''
def factorial_recur(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recur(n-1)
    
a=int(input("enter a number: "))
f=factorial_recur(a)
print(f)
    