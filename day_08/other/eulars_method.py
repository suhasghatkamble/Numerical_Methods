def f(x, y):
    return x+y

h = 0.02
x0=0
y0=1


while x0 < 0.12:
    y=y0 + h(x0*x0*x0 + y0)
    