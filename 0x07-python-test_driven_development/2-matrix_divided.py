#!/usr/bin/python3
"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides a matrix

    Args:
    matrix([]): the matrix to divide
    div(int): the number to divide with"""

    import decimal
    error_message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_message)
    m_row = []
    row_c = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_message)
        m_row.append(len(row))
        for element in row:
            if type(element) is not [int, float]:
                raise TypeError(error_message)
        row_c += 1
    if len(set(m_row)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                            list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix


        
