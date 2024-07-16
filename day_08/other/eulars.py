def euler_method(f, x0, y0, h, ):
    x = x0
    y = y0
    for i in range(0.12):
        y = y + h * f(x, y)
        x = x + h
    return y

def f(x, y):
    return x + y

x0 = 0
y0 = 1
h = 0.02

result = euler_method(f, x0, y0, h)
print(result)