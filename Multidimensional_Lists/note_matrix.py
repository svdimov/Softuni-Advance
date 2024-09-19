#  #create matrix
# matrix = []
# for row in range(3):
#     matrix.append([])
#     for cow in range(1,4):
#         matrix[row].append(cow)
# print(matrix)
# Comprehension Matrix
# matrix = [[0 for cow in range(1,4)]for row in range(3)]
# print(matrix)

# ------------------------------

# Flattend comprehension - унпакване на матрицата
# matrix = [[1,2,3],[4,5,6]]
# # un_pack = [cow for row in matrix for cow in row] #flattend - разархивиране на матрица като главния цикъл е първи
# # Case 2 use extend()
# m =[]
# [m.extend(l) for l in matrix]
# print(m)

# ------------------------------------------------------

#  при назъбени матрици ползваме индекси в цикъла за валидиране
# Както и при промяна на стойностите на елементите във матрицата !!!!!! Важно


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)): #ползваме райндж от матрицата
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()
result = '\n'.join([' '.join(map(str, row)) for row in matrix])
print(result)