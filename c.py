import functions as f
import numpy as np


# c) demonstrating that ld(rd (R)) is the same as rd(ld(R)) for all 11 relationships
def prt1_c_disjoin():
    disjoin = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])

    print("ld(rd (R))")
    print("For: DISJOIN")
    print(disjoin)
    x = f.rt_dual(disjoin)
    print("-> to inside with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to EMBRACE with left dual.")
    print(x)

    print("rd(ld(R))")
    disjoin = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
    print('For: DISJOIN')
    print(disjoin)
    y = f.lft_dual(disjoin)
    print('-> to contains with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to EMBRACE with right dual.')
    print(y)
    print("\n")


def prt1_c_embrace():
    embrace = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])

    print("ld(rd (R))")
    print("For: EMBRACE")
    print(embrace)
    x = f.rt_dual(embrace)
    print("-> to contains with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to DISJOIN with left dual.")
    print(x)

    print("rd(ld(R))")
    embrace = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])
    print('For EMBRACE')
    print(embrace)
    y = f.lft_dual(embrace)
    print('-> to inside with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to DISJOIN with right dual.')
    print(y)
    print("\n")


def prt1_c_attach():
    attach = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    print("ld(rd (R))")
    print("For: ATTACH")
    print(attach)
    x = f.rt_dual(attach)
    print("-> to equals with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to ATTACH with left dual.")
    print(x)

    print("rd(ld(R))")
    attach = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    print('For: ATTACH')
    print(attach)
    y = f.lft_dual(attach)
    print('-> to equals with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to ATTACH with right dual.')
    print(y)
    print("\n")


def prt1_c_entwined():
    entwined = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])

    print("ld(rd (R))")
    print("For: ENTWINED")
    print(entwined)
    x = f.rt_dual(entwined)
    print("-> to covers with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to MEET with left dual.")
    print(x)

    print("rd(ld(R))")
    entwined = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])
    print('For: ENTWINED')
    print(entwined)
    y = f.lft_dual(entwined)
    print('-> to coveredBy with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to MEET with right dual.')
    print(y)
    print("\n")


def prt1_c_meet():
    meet = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1]])

    print("ld(rd (R))")
    print("For: MEET")
    print(meet)
    x = f.rt_dual(meet)
    print("-> to coveredBy with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to ENTWINED with left dual.")
    print(x)

    print("rd(ld(R))")
    meet = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1]])
    print('For: MEET')
    print(meet)
    y = f.lft_dual(meet)
    print('-> to covers with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to ENTWINED with right dual.')
    print(y)
    print("\n")


def prt1_c_overlap():
    overlap = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    print("ld(rd (R))")
    print("For: OVERLAP")
    print(overlap)
    x = f.rt_dual(overlap)
    print("-> to OVERLAP with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to OVERLAP with left dual.")
    print(x)

    print("rd(ld(R))")
    overlap = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print('For: OVERLAP')
    print(overlap)
    y = f.lft_dual(overlap)
    print('-> to overlap with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to OVERLAP with right dual.')
    print(y)
    print("\n")


def prt1_c_coveredBy():
    coveredBy = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])

    print("ld(rd (R))")
    print("For: COVEREDBY")
    print(coveredBy)
    x = f.rt_dual(coveredBy)
    print("-> to meet with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to COVERS with left dual.")
    print(x)

    print("rd(ld(R))")
    coveredBy = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
    print('For: COVEREDBY')
    print(coveredBy)
    y = f.lft_dual(coveredBy)
    print('-> to entwined with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to COVERS with right dual.')
    print(y)
    print("\n")


def prt1_c_covers():
    covers = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])

    print("ld(rd (R))")
    print("For: COVERS")
    print(covers)
    x = f.rt_dual(covers)
    print("-> to meet with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to COVEREDBY with left dual.")
    print(x)

    print("rd(ld(R))")
    covers = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    print('For: COVERS')
    print(covers)
    y = f.lft_dual(covers)
    print('-> to meet with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to COVEREDBY with right dual.')
    print(y)
    print("\n")


def prt1_c_inside():
    inside = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])

    print("ld(rd (R))")
    print("For: INSIDE")
    print(inside)
    x = f.rt_dual(inside)
    print("-> to disjoin with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to CONTAINS with left dual.")
    print(x)

    print("rd(ld(R))")
    inside = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
    print('For: INSIDE')
    print(inside)
    y = f.lft_dual(inside)
    print('-> to embrace with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to CONTAINS with right dual.')
    print(y)
    print("\n")


def prt1_c_equals():
    equals = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    print("ld(rd (R))")
    print("For: EQUALS")
    print(equals)
    x = f.rt_dual(equals)
    print("-> to attach with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to EQUALS with left dual.")
    print(x)

    print("rd(ld(R))")
    equals = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print('For: EQUALS')
    print(equals)
    y = f.lft_dual(equals)
    print('-> to attach with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to EQUALS with right dual.')
    print(y)
    print("\n")


def prt1_c_contains():
    contains = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])

    print("ld(rd (R))")
    print("For: CONTAINS")
    print(contains)
    x = f.rt_dual(contains)
    print("-> to embrace with right dual.")
    print(x)
    x = f.lft_dual(x)
    print("-> to INSIDE with left dual.")
    print(x)

    print("rd(ld(R))")
    contains = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
    print('For: CONTAINS')
    print(contains)
    y = f.lft_dual(contains)
    print('-> to disjoin with left dual.')
    print(y)
    y = f.rt_dual(y)
    print('-> to INSIDE with right dual.')
    print(y)
    print("\n")
