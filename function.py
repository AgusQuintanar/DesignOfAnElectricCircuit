import math

def get_func(t,l,c,ratio):
    return lambda x: math.e**((-t*x)/(2*l)) * math.cos(t*math.sqrt(1/(l*c)-(x/(2*l))**2)) - ratio

def get_range(l,c):
    return 0, math.sqrt(4*l/c)
