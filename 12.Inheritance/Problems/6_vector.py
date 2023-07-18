''' Write ___str___() method to pront the vector
        3i + 8j + 10k
    Assume vector of dimension 3 for this problem'''

class vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        return f" {self.vec[0]}i + {self.vec[2]}j + {self.vec[2]}k"
    

v1 = vector([1,4,5])
v2 = vector([2,5,0])
print(v1)
print(v2)