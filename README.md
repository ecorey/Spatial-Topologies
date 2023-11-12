# Three operations that apply to the eleven region-region relations R in S2 as shown in the [Point-Set Topological Spatial Relations](http://www.dpi.inpe.br/gilberto/references/egenhofer_point_set.pdf) are as follows:

- **converse (conv)**
- **leftDual (ld)**
- **rightDual (rd)**

# Each of the three operations given above will give a relation as a result, and the operations can also be applied recursively.

# This program verifies exhaustively (for each of the eleven relations) that:

- 1.1a: conv(ld(R)) is equivalent to ld(conv(R))

- 1.1b: conv(rd(R)) is equivalent to rd(conv(R))

- 1.1c: ld(rd (R)) is equivalent to rd(ld(R))

# This program also verifies exhaustively (for each of the eleven relations) that:

- 1.2a: rd(conv(ld(R))) is equivalent to rd(ld(conv(R)))

- 1.2b: ld(conv(rd(R))) is equivalent to ld(rd(conv(R)))

- 1.2c: conv(ld(rd(R))) is equivalent to conv(rd(ld(R)))

# Conclusions

- 1.3: From the results in 1.1 and 1.2

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
