# Write a Python function that takes an integer as input
# and returns a second order polynomial function using
# the input integer as a seed for a numpy random number generator.
import numpy as np
import time

def generate_polynomial(seed = 0, order = 2):
    if seed == 0:
        seed = time.time_ns()
    rng = np.random.default_rng(seed)
    r = []
    for i in range(order):
        if i == 0:
            r.append(rng.random()*10.2 - 7.5)
        if i == 1:
            r.append(r[0] + rng.random()*1.5 + 1.0)
        if i > 1:
            r.append(r[i-1] + (-1)**i*rng.random()*1.5)
    p = np.round(np.poly(r), 4)/9.87
    return p

def lab_1_problem_1(x, seed = 0):
    p = generate_polynomial(seed, 2)
    return np.polyval(p, x)

def lab_1_problem_3(x, seed = 0):
    p = generate_polynomial(seed, 3)
    return np.polyval(p, x)

def lab_2_problem_1(x, seed = 0):
    p = generate_polynomial(seed, 4)
    return np.polyval(p, x)

def lab_2_problem_2(seed = 0):
    if seed == 0:
        seed = time.time_ns()
    rng = np.random.default_rng(seed)
    k = rng.integers(20, 50).item()/10.0
    c = rng.integers(200, 700).item()/100.0

    md_txt = r"""
In this problem your task is to graphically find the intersection points of the two functions.

The first functions is $$ f(x) = \sqrt{""" + f"{k:.1f}" + r"""x} $$ and 
the second function is $$ g(x) = (x - """ + f"{c:.2f}" + r""")^2 $$

Use the domain $x \in [0, 10]$."""

    return md_txt 

def lab_3_problem_1(seed = 0):
    if seed == 0:
        seed = time.time_ns()
    rng = np.random.default_rng(seed + 123)
    x0 = rng.integers(-20, 10).item()/10.0
    w = rng.integers(2, 5).item()

    txt = f"""
In this problem your task is to create and plot a piecwise
continuous function in range $ x \in [-10, 10] $.

The function is defined as:<br>

$$ f(x)  = \\begin{{cases}} 
0 & x < {x0:.1f}  \\\\ 
{-x0:.1f} + x & {x0:.1f} \leq x < {x0+w:.1f} \\\\
{x0+2*w:.1f} - x & {x0+w:.1f} \leq x < {x0+2*w:.1f} \\\\ 
0 & x \\geq {x0+2*w:.1f} 
\\end{{cases}} $$

Draw the function within the given range of x.

Remember to decorate the plots with title, axis labels, and a legend. Add also grid
lines to the plots to make them easier to read."""

    return txt 

def lab_3_problem_2(seed = 0):
    if seed == 0:
        seed = time.time_ns()
    p = generate_polynomial(seed + 10000, 3)
    p = np.round(p, 2)
    rng = np.random.default_rng(seed + 10000)
    x0 = rng.integers(-80, -40).item()/10.0
    x1 = rng.integers(40, 80).item()/10.0
    y0 = np.polyval(p, x0)
    y1 = np.polyval(p, x1)  

    txt = f"""
In this problem your task is to create and plot a piecwise
continuous function in range $ x \in [-10, 10] $.

The function is defined as:<br>

$$ f(x)  = \\begin{{cases}} 
{y0:.2f} & x < {x0}  \\\\ 
{p[0]}x^3 + {p[1]}x^2 + {p[2]}x + {p[3]} & {x0} \\leq x < {x1} \\\\
{y1:.2f} & x \\geq {x1} 
\\end{{cases}} $$

Draw the function within the given range of x.

Remember to decorate the plots with title, axis labels, and a legend. Add also grid
lines to the plots to make them easier to read."""

    return txt 
