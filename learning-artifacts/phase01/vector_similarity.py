import math

a = [2, 4]
b = [4, 8]

dot_production = (a[0] * b[0]) + (a[1] * b[1])
magnitude_a = math.sqrt(a[0]**2 + a[1]**2)
magnitude_b = math.sqrt(b[0]**2 + b[1]**2)
cosine_calculation = magnitude_a * magnitude_b

cosine_similarity = dot_production / cosine_calculation

print(cosine_calculation)