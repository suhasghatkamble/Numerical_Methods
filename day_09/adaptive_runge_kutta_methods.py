import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -2*y

def rk4(f, t, y, h):
    # Perform single step of RK4 method
    
    k1 = h * f(t, y)
    k2 = h *f(t + 0.5 *h, y + 0.5 * k1)
    k3 = h *f(t + 0.5 *h, y + 0.5 * k2)
    k4 = h *f(t + h, y + k3)
    return y + k1/6 + k2/3 + k3/3 + k4/6

def adaptive_rk4(f, x0, y0, tf, h0, tol):
    # Adaptive stepsize control for RK4 method
    # tf: Final time
    x = x0
    y = y0
    h = h0
    X=[x]
    ys=[y]
    while x<tf:
        y_step = rk4(f,x,y,h)
        y_double_step=rk4(f,x,y,h/2)
        y_double_step=rk4(f,x + h/2,y_double_step,h/2)
        error=(y_double_step - y_step)/10.0
        
        if error<tol:
            x +=h
            y=y_double_step
            X.append(x)
            ys.append(y)
            h = h * min(2,(tol/error)**0.20)
        else:
            h = h * max(0.5,(tol/error)**0.20)
    return np.array(X), np.array(ys)

#x=0~10 initial value y0=1, initial step size = 0.1, tolerance = 1e-5
t_vals, y_vals=adaptive_rk4(f,0,1,10,0.1,1e-5)