def question1(n):
    return (n + 1) % 6 == 0 #remainder check
def main1():
    try:
        user = input("enter an integer between 1 and 100 for question 1: ")#user input
        number = int(user)
        if not(1 <= number <= 100):
            print("enter a number between 1 and 100: ")
            return
        if question1(number):
            print("true")
        else:
            print("false")
    except ValueError:
        print("enter a number between 1 and 100: ")#1-100 only
main1()
import math
def question2(x):
    if x < 0:
        raise ValueError("x must be non-negative to calculate the square root.")#failsafe for negatives
    if 3 * x - 7 == 0:
        raise ValueError("the denominator 3x - 7 must not equal zero.") #failsafe for divide by 0
    numerator = math.sqrt(x) + 3 * (x ** 5)
    denominator = 3 * x - 7
    return numerator / denominator#answer
def main2():
    try:
        userinput2 = input("enter a number x for question 2: ")#user input
        x = float(userinput2)
        result = question2(x)
        print(f"f({x}) = {result}")
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("invalid input")
        else:
            print(f"{e}")
    except Exception:
        print("invalid input")#failsafes for invalid inputs
main2()
import sympy as sp
def question3(a, b, c, d):
    x = sp.symbols('x')
    f = a * sp.sin(b * x) + c * sp.exp(d * x)
    f5 = f.subs(x, 5)
    f3diff = sp.diff(f, x, 3)
    fintegral = sp.integrate(f, (x, 2 * sp.pi, sp.sqrt(6)))
    return [f5, f3diff, fintegral]
def main3():
    print("enter values for a, b, c, and d for question 3")#user input
    try:
        a = float(input("enter value for a: "))
        b = float(input("enter value for b: "))
        c = float(input("enter value for c: "))
        d = float(input("enter value for d: "))
        result = question3(a, b, c, d)
        print("\nResults:")
        print(f"(a) f(5) = {result[0]}")
        print(f"(b) d^3(f(x))/dx^3 = {result[1]}")
        print(f"(c) integral of f(x) from 2pi to sqrt(6) = {result[2]}")
    except ValueError:
        print("enter valid values for a, b, c, and d.")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")#failsafes
main3()
def question4(n):
    primes = []
    current = math.floor(n) + 1#makes sure non integers work
    while len(primes) < 3:
        if sp.isprime(current):
            primes.append(current)
        current += 1
    return primes
def main4():
    try:
        n = float(input("enter a number for question 4: "))#user input
        result = question4(n)
        print(f"the next three primes greater than {n} are: {result}")
    except ValueError:
        print("enter a valid number.")#failsafe
main4()
