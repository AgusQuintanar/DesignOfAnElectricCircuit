t = 1
l = 1
c = 1
ratio = .1

fun = lambda x: e**(-1*t*x/(2*l))*math.cos(t*math.sqrt(1/(l*c)-(x/(2*l))**2)) - ratio

start = 0
end = math.sqrt(4*l/c)
