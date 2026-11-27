matrix = [
    [2, 1],
    [3, 4]
]

vector = [5, 2]
transformed_vector = []
for mat in matrix:
   
   row_one_1 = mat[0] * vector[0] 
   row_one_2 = mat[1] * vector[1]
   added01 = row_one_1 + row_one_2
   transformed_vector.append(added01)

#    row_two_1 = mat[0] * vector[0]
#    row_two_2 = mat[1] * vector[1]
#    added02 = row_two_1 + row_two_2
# transformed_vector.append(added01)
    

print(transformed_vector)
