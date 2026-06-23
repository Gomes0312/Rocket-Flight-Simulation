import math

#Data
m = 2350
g = 9.81
T = 163000
Da = 0.37
Dc = 0.28
p = 1.225
Aa = 0.3
Ac = 0.91
dt = 0.05
D = (Dc + Da)
P = m*g

h = 0
v = 0
t = 0

for i in range (177):
a = (T - D - P) / m
Dc = 0.5 * p * v**2 * Dc * Ac
Da = 0.5 * p * v**2 * Da * Aa
t = t+dt
v = v+a*dt
h = h+v*dt
if t = 8.85
print (h,v,t)
