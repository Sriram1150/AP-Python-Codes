class Vector():
    def __init__(self, vec):
        self.vector = vec

    def __str__(self):
        return f"{len(self.vector)}-dimensional vector: {self.vector}"
    
    def __mul__(self,n):
        new = []
        for i in self.vector:
            new.append(i*n)
        return new
    
    def __add__(self,n):
        new = []
        for i in range(len(self.vector)):
            new.append(self.vector[i] + n.vector[i])
        return new

    def __sub__(self,n):
        new = []
        for i in range(len(self.vector)):
            new.append(self.vector[i] - n.vector[i])
        return new

    def __and__(self,n):
        sum = 0
        for i in range(len(self.vector)):
            sum += (self.vector[i] * n.vector[i])
        return sum

v1 = Vector([1,2,3])
v2 = Vector([4,5,6])
print(v1)
print(v1*2)
print(v1 & v2)
print(v1 + v2)
print(v1 - v2)