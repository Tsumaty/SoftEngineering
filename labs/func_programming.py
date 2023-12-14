import math

def f(xLam, yLam):
    return xLam + yLam

x = lambda xDer: xDer ** 2 + 1
y = lambda yDer: math.sin(yDer ** 2) - 1

print(f(x(3), y(5)))
