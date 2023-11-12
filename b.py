import functions as f
import numpy as np


# b) demonstrating that conv(rd(R)) is the same as rd(conv(R)) for all 11 relationships
def prt1_b_disjoin():
    disjoin = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])

    print("conv(rd(R))")
    print("For: DISJOIN")
    print(disjoin)
    x = f.rt_dual(disjoin)
    print("-> to inside with right dual.")
    print(x)
    f.converse(x)
    print("-> to CONTAINS with converse.")
    print(x)

    print("rd(conv(R))")
    disjoin = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
    print('For: DISJOIN')
    print(disjoin)
    y = f.converse(disjoin)
    print('-> to disjoin with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to INSIDE with right dual.')
    print(y)
    print("\n")


def prt1_b_embrace():
    embrace = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])

    print("conv(rd(R))")
    print("For: EMBRACE")
    print(embrace)
    x = f.rt_dual(embrace)
    print("-> to contains with right dual.")
    print(x)
    f.converse(x)
    print("-> to INSIDE with converse.")
    print(x)

    print("rd(conv(R))")
    embrace = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]])
    print('For EMBRACE')
    print(embrace)
    y = f.converse(embrace)
    print('-> to embrace with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to CONTAINS with right dual.')
    print(y)
    print("\n")



def prt1_b_attach():
    attach = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    print("conv(rd(R))")
    print("For: ATTACH")
    print(attach)
    x = f.rt_dual(attach)
    print("-> to equal with right dual.")
    print(x)
    f.converse(x)
    print("-> to EQUAL with converse.")
    print(x)

    print("rd(conv(R))")
    attach = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    print('For: ATTACH')
    print(attach)
    y = f.converse(attach)
    print('-> to attach with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to EQUAL with right dual.')
    print(y)
    print("\n")


def prt1_b_entwined():
    entwined = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])

    print("conv(rd(R))")
    print("For: ENTWINED")
    print(entwined)
    x = f.rt_dual(entwined)
    print("-> to covers with right dual.")
    print(x)
    f.converse(x)
    print("-> to COVEREDBY with converse.")
    print(x)

    print("rd(conv(R))")
    entwined = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])
    print('For: ENTWINED')
    print(entwined)
    y = f.converse(entwined)
    print('-> to entwined with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to COVERS with right dual.')
    print(y)
    print("\n")


def prt1_b_meet():
    meet = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1]])

    print("conv(rd(R))")
    print("For: MEET")
    print(meet)
    x = f.rt_dual(meet)
    print("-> to coverdBy with right dual.")
    print(x)
    f.converse(x)
    print("-> to COVERS with converse.")
    print(x)

    print("rd(conv(R))")
    meet = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1]])
    print('For: MEET')
    print(meet)
    y = f.converse(meet)
    print('-> to meet with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to COVEREDBY with right dual.')
    print(y)
    print("\n")


def prt1_b_overlap():
    overlap = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    print("conv(rd(R))")
    print("For: OVERLAP")
    print(overlap)
    x = f.rt_dual(overlap)
    print("-> to OVERLAP with right dual.")
    print(x)
    f.converse(x)
    print("-> to OVERLAP with converse.")
    print(x)

    print("rd(conv(R))")
    overlap = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print('For: OVERLAP')
    print(overlap)
    y = f.converse(overlap)
    print('-> to OVERLAP with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to OVERLAP with right dual.')
    print(y)
    print("\n")


def prt1_b_coveredBy():
    coveredBy = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])

    print("conv(rd(R))")
    print("For: COVEREDBY")
    print(coveredBy)
    x = f.rt_dual(coveredBy)
    print("-> to meet with right dual.")
    print(x)
    f.converse(x)
    print("-> to MEET with converse.")
    print(x)

    print("rd(conv(R))")
    coveredBy = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
    print('For: COVEREDBY')
    print(coveredBy)
    y = f.converse(coveredBy)
    print('-> to covers with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to ENTWINED with right dual.')
    print(y)
    print("\n")



def prt1_b_covers():
    covers = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])

    print("conv(rd(R))")
    print("For: COVERS")
    print(covers)
    x = f.rt_dual(covers)
    print("-> to entwined with right dual.")
    print(x)
    f.converse(x)
    print("-> to ENTWINED with converse.")
    print(x)

    print("rd(conv(R))")
    covers = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
    print('For: COVERS')
    print(covers)
    y = f.converse(covers)
    print('-> to coveredBy with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to MEET with right dual.')
    print(y)
    print("\n")


def prt1_b_inside():
    inside = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])

    print("conv(rd(R))")
    print("For: INSIDE")
    print(inside)
    x = f.rt_dual(inside)
    print("-> to disjoin with right dual.")
    print(x)
    f.converse(x)
    print("-> to DISJOIN with converse.")
    print(x)

    print("rd(conv(R))")
    inside = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
    print('For: INSIDE')
    print(inside)
    y = f.converse(inside)
    print('-> to contains with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to EMBRACE with right dual.')
    print(y)
    print("\n")



def prt1_b_equals():
    equals = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    print("conv(rd(R))")
    print("For: EQUALS")
    print(equals)
    x = f.rt_dual(equals)
    print("-> to attach with right dual.")
    print(x)
    f.converse(x)
    print("-> to ATTACH with converse.")
    print(x)

    print("rd(conv(R))")
    equals = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print('For: EQUALS')
    print(equals)
    y = f.converse(equals)
    print('-> to equals with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to ATTACH with right dual.')
    print(y)
    print("\n")



def prt1_b_contains():
    contains = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])

    print("conv(rd(R))")
    print("For: CONTAINS")
    print(contains)
    x = f.rt_dual(contains)
    print("-> to embrace with right dual.")
    print(x)
    f.converse(x)
    print("-> to EMBRACE with converse.")
    print(x)

    print("rd(conv(R))")
    contains = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
    print('For: CONTAINS')
    print(contains)
    y = f.converse(contains)
    print('-> to inside with converse.')
    print(y)
    y = f.rt_dual(y)
    print('-> to DISJOIN with right dual.')
    print(y)
    print("\n")



