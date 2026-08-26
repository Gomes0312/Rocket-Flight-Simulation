import math
#test for variable gravity
dt = 0.001
Bt = 9.999 #Tempo de queima
R = 6*10**5
g = 9.81
#Initial values:
v = 100
h = t = vi = vf = vm = 0

while (v>0):
h_rel = h/R
vi = v
g_nova = g/(1+h_rel)**2
v = v-(g_nova*dt)
vf = v
vm = (vi+vf)/2
h = h+(vm*dt)
t = t+dt

print(v,t,h)
