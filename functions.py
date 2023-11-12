def lft_dual(matrix):
    """Returns the left dual of a given matrix."""
    temp = [0, 0, 0]
    temp[0] = matrix[0][0]
    temp[1] = matrix[0][1]
    temp[2] = matrix[0][2]

    matrix[0][0] = matrix[2][0]
    matrix[0][1] = matrix[2][1]
    matrix[0][2] = matrix[2][2]

    matrix[2][0] = temp[0]
    matrix[2][1] = temp[1]
    matrix[2][2] = temp[2]

    return matrix

# print(lft_dual(im.embrace))

def rt_dual(matrix):
    """Returns the right dual of a given matrix."""
    temp = [0, 0, 0]
    temp[0] = matrix[0][0]
    temp[1] = matrix[1][0]
    temp[2] = matrix[2][0]

    matrix[0][0] = matrix[0][2]
    matrix[1][0] = matrix[1][2]
    matrix[2][0] = matrix[2][2]

    matrix[0][2] = temp[0]
    matrix[1][2] = temp[1]
    matrix[2][2] = temp[2]

    return matrix


def converse(matrix):
    """Returns the converse of a given matrix."""
    if (matrix[1][0] == matrix[0][1]) and (matrix[2][0] == matrix[0][2]) and (matrix[2][1] == matrix[1][2]):
        # symmetrical matrices will return the matrix
        return matrix
    elif (matrix[1][0] != matrix[0][1]) and (matrix[2][0] != matrix[0][2]) and (matrix[2][1] != matrix[1][2]):
        # converse matrices will return the converse matrix. For example, meet will
        # return a meet matrix, but inside will return contains, and contains will return inside.
        temp = [0, 0, 0]
        temp[0] = matrix[0][1]
        temp[1] = matrix[0][2]
        temp[2] = matrix[1][2]

        matrix[0][1] = matrix[1][0]
        matrix[0][2] = matrix[2][0]
        matrix[1][2] = matrix[2][1]

        matrix[1][0] = temp[0]
        matrix[2][0] = temp[1]
        matrix[2][1] = temp[2]

        return matrix


def double_dual(matrix):
    """Returns the double dual of a given matrix."""
    x = lft_dual(matrix)
    y = rt_dual(x)
    return y



