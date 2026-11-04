class Vectors:
    def __init__(self, components):
        self.components = list(components)
        self.dimention = len(self.components)

    def __add__(self, other):
        return Vectors([a + b for a,b in zip(self.components, other.components)])
    

a = Vectors([1,2,3])
b = Vectors([4,5,6])
c = a+b
print(c.components)