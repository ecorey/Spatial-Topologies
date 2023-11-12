# Three operations that apply to the eleven region-region relations R in S2 as shown in the [Point-Set Topological Spatial Relations](http://www.dpi.inpe.br/gilberto/references/egenhofer_point_set.pdf) are as follows:

- **converse (conv)**
- **leftDual (ld)**
- **rightDual (rd)**

_**Each of these three operations given will also produce a relation as a result, and the operations can also be applied recursively.**_

# This program verifies exhaustively (for each of the eleven relations {R} ) that:

- a: conv(ld(R)) is equivalent to ld(conv(R))

- b: conv(rd(R)) is equivalent to rd(conv(R))

- c: ld(rd (R)) is equivalent to rd(ld(R))

# This program also verifies exhaustively (for each of the eleven relations {R} ) that:

- d: rd(conv(ld(R))) is equivalent to rd(ld(conv(R)))

- e: ld(conv(rd(R))) is equivalent to ld(rd(conv(R)))

- f: conv(ld(rd(R))) is equivalent to conv(rd(ld(R)))

# Conclusions

- Conclusions: From the results in (a, b, c) and (d, e, f)

---

---

# The eleven region-region relations R in S2 and their intersection matrix:

    embrace = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])

    attach = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    disjoin = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])

    entwined = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])

    meet = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1]])

    overlap = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    coveredBy = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])

    covers = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])

    inside = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])

    equals = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    contains = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])

# Operations

# Left Dual

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

# Right Dual

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

# Converse

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

# Double Dual

    def double_dual(matrix):
        """Returns the double dual of a given matrix."""
        x = lft_dual(matrix)
        y = rt_dual(x)
        return y
