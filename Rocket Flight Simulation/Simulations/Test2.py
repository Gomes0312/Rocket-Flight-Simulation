import math

#Data
m = 2350
T = 163000
Da = 0.37
Dc = 0.28
p = 1.225
Aa = 0.3
Ac = 0.91
dt = 0.05
G = 6.67 * 10**-11
R = 6378137
M = 5.97 * 10**24
h = 0
v = 0
t = 0

#formulas
D = (Dc + Da)
P = m*g
g = G * M / (h + R)**2

for i in range (177):
a = (T - D - P) / m
Dc = 0.5 * p * v**2 * Dc * Ac
Da = 0.5 * p * v**2 * Da * Aa
v = v+a*dt

a = - D - P / m
t = t+dt
h = h+v*dt
v = v+a*dt
print (h,v,t)
