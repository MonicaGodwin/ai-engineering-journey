class Vectors:
    def __init__(self, components):
        self.components = list(components)
        self.dimention = len(self.components)

    def __add__(self, other):
        return Vectors([a + b for a,b in zip(self.components, other.components)])
    
    def dot(self, other):
        return sum(a*b for a,b in zip(self.components, other.components))
    
    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        return Vectors([x / mag for x in self.components])
    
    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())
    
    def __repr__(self):
        return f"Vector({self.components})"


a = Vectors([1,2,3])
b = Vectors([4,5,6])
d = a + b 
c = a.dot(b)
print(d.components)
print(c)
print(f"{a.magnitude():.4f}")
print(f"{a.cosine_similarity(b):.4f}")

