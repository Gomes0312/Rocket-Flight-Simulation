import math
#test for constant gravity
dt = 0.001
a = g = 10
Bt = 9.999 #Tempo de queima
#Initial values:
v = 100
h = t = vi = vf = vm = 0

while (v>0):
vi = v
v = v-(a*dt)
vf = v
vm = (vi+vf)/2
h = h+(vm*dt)
t = t+dt

print(v,t,h)
