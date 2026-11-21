# vector = [3, 2]

# x = vector[0]
# y = vector[1]

# magnitude = (x ** 2 + y ** 2)**0.5

# print(magnitude)


import math

a = [2, 4]
b = [4, 8]

# magnitude_a = a[0]**0.5 + a[1]**0.5
# magnitude_b = b[0]**0.5 + b[1]**0.5

magnitude_a = math.sqrt(a[0]) + math.sqrt(a[1])
magnitude_b = math.sqrt(b[0]) + math.sqrt(b[1])

print(magnitude_a)
print(magnitude_b)