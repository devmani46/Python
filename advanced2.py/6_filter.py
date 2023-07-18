#syntax : list(filter(unction, list))
def greater_than_5(num):
    if num>5:
        return True
    else:
        return False


a= lambda num:num>10    
l = [2,1,3,45,234,53,12,21,8]
print(list(filter(greater_than_5,l))) 
print(list(filter(a,l))) 
