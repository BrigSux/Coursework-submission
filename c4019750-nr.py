import sympy as sp
def nr(func, funcp, x0, x, tol=1e-6, itmax=100):
    """
    does the newton raphson method iteratively to get root
    func = function we are finding root for
    funcp = derivative of the function
    x0 = initial value
    tol = the tolerance for convergence
    itmax = max number of iterations
    float = root estimated
    """
    x_n = x0
    for _ in range(itmax): #find value and derivative at guess
        fval = func.subs(x, x_n)
        fpval = funcp.subs(x, x_n)
        if abs(fpval) < 1e-12: #avoid divide by 0
            print("derivative too small, iteration stopped")
            return None
        x_n1 = x_n - fval / fpval
        if abs(x_n1 - x_n) < tol: #does it converge?
            print(f"converged to: {x_n1}")
            return x_n1#yes
        x_n = x_n1
    print("done max iterations, no convergence")#no
    return None
def mainnr():
    try:
        x = sp.symbols('x')#user input
        x0 = float(input("enter an initial value: "))
        f = sp.sin(2 * x) - (x**3 - 3*x**2 - 6*x + 7)
        fp = sp.diff(f, x)
        root = nr(f, fp, x0, x)
        if root is not None:
            print(f"root: {root}")
    except ValueError:
        print("enter a valid initial guess.")#failsafes
mainnr()
