'''Overide the ___len___() method on Vector of problem 5 
to display the dimension of the vector'''

class vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)

    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i] 
        return sum

    def __len__(self):
        return len(self.vec)

v1 = vector([1,4,7])
v2 = vector([2,5])
print(len(v1))
print(len(v2))