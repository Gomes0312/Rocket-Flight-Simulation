import math
#test for variables in function of dt
dt = 0.001
a = 10
Bt = 9.999 #Tempo de queima
#Initial values:
v = h = t = vi = vf = vm = 0

while (t<Bt):
vi = v
v = v+(a*dt)
vf = v
vm = (vi+vf)/2
h = h+(vm*dt)
t = t+dt
print(v,t,h)
