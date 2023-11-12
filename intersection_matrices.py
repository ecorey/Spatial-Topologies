import numpy as np

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

