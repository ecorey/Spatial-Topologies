# Three operations that apply to the eleven region-region relations R in S2 are:

- **converse (conv)**
- **leftDual (ld)**
- **rightDual (rd)**

# Since each of the three operations yields a relation as the result, these operations can be applied recursively.

# This program verifies exhaustively (for all eleven relations) that:

- 1.1a: conv(ld(R)) is the same as ld(conv(R))

- 1.1b: conv(rd(R)) is the same as rd(conv(R))

- 1.1c: ld(rd (R)) is the same as rd(ld(R))

# These three operations can also be applied three times in a row. This program verifies exhaustively (for all eleven relations) that:

- 1.2a: rd(conv(ld(R))) is the same as rd(ld(conv(R)))

- 1.2b: ld(conv(rd(R))) is the same as ld(rd(conv(R)))

- 1.2c: conv(ld(rd(R))) is the same as conv(rd(ld(R)))

# Conclusions

- 1.3: From the results in 1.1 and 1.2
