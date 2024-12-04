import sympy as sp
def matrix():
    print("enter the values for A:")#user input
    a = float(input("enter value for a: "))
    b = float(input("enter value for b: "))
    c = float(input("enter value for c: "))
    d = float(input("enter value for d: "))
    e = float(input("enter value for e: "))
    f = float(input("enter value for f: "))
    g = float(input("enter value for g: "))
    h = float(input("enter value for h: "))
    i = float(input("enter value for i: "))
    MatA = sp.Matrix([[a, b, c], [d, e, f], [g, h, i]])#matrix
    return MatA
def matrixop():#operations
    MatA = matrix()
    try:
        MatAinv = MatA.inv()#inverse
        print("\ninverse of A:")
        sp.pprint(MatAinv)
    except sp.LinAlgError:
        print("\nA is not inversible")#failsafe
    eigenv = MatA.eigenvals()
    print("\neigenvalues of A:")#eigenvalues
    sp.pprint(eigenv)
    eigenve = MatA.eigenvects()#eigenvectors
    print("\neigenvectors of A:")
    for vec in eigenve:
        print(f"eigenvalue: {vec[0]}, eigenvector: {vec[2]}")
    try:
        P, D = MatA.diagonalize()#diagonalise
        print("\ndiagonalization of A (P * D * P_inv):")
        print(f"P matrix (eigenvectors):\n{P}")
        print(f"diagonal matrix D:\n{D}")
    except ValueError:
        print("\nA cannot be diagonalized.")#failsafe
matrixop()
