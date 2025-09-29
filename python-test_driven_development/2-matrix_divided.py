"""Define a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""

    row_size = None
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for num in matrix:
        if not num or not isinstance(num, list):
            raise TypeError(message)

        for n in num:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(num)
        elif row_size != len(num):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
