# Solves the root of a function using bisection method
# 
# Example
# funct = lambda x : x **2 -2
# solve(funct, 0, 3, 100, 0.01 // output 1.41...
#

def solve(fun, l, r, max_iter, de):

    i, x_l, x_r, ea, x_old = 0,l,r,101,l

    while i < max_iter and ea > de :
        x_m = (x_l + x_r) / 2
        
        f_m = fun(x_m)
        f_l = fun(x_l)

        if abs(x_m) > 0.001 :
            ea = abs((x_m - x_old) / x_m) * 100

        test = f_m * f_l

        if test < 0:
            x_r = x_m
        elif test > 0:
            x_l = x_m
        else:
            ea = 0

        i += 1
        x_old = x_m

    return x_old
