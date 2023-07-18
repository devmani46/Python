''' Create a class C-2d vector and use it to create another class
representing a 3-d vector'''

class C2dvector :
    def __init__(self,i,j):
        self.icap= i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}"

class C3dvector(C2dvector):
    def __init__(self,i,j,k):
        super(). __init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d= C2dvector(1,3)
v3d = C3dvector(1,9,7)
print(v2d)
print(v3d)

