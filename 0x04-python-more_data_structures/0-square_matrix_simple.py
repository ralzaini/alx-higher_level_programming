def square_matrix_simple(matrix=[]):
    square_mat = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return square_mat
