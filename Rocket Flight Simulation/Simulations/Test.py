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
MaxSpeed = []
#Initial Values
h = 0
v = 0
t = 0
#Propulsion
for i in range (177):
a = (T - D - P) / m
Dc = 0.5 * p * v**2 * Dc * Ac
Da = 0.5 * p * v**2 * Da * Aa
t = t+dt
v = v+a*dt
h = h+v*dt

MaxSpeed.append(f"{v:.2f}")
#No Propulsion
while (v>0):
a = (- D - P) / m
Dc = 0.5 * p * v**2 * Dc * Ac
Da = 0.5 * p * v**2 * Da * Aa
t = t+dt
v = v+a*dt
h = h+v*dt

print(f"Max altitude = {h:.2f} meters | Max speed = {MaxSpeed}m/s | Time of flight = {t:.2f} seconds")
