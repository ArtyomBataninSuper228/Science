import math

f1 = 39800
r1 = 0.10725
f2 = 39890
r2 = 0.28215
l = (r2-r1)/20
c = l*(f1+f1)/2
dr = 0.025/1000
df = f1*10**-5 + 0.5#90
#print(df)
#df = 90
n = 20


dC = 2*dr*f1/n + df*(r2-r1)/n
print(f"C = {round(c,2)} +- {round(dC, 2)}")
print(f"l = {l*1000}мм +- {2*dr*1000}мм")
print(2*dr/(r2-r1)*10**3, df/f1*10**3)

#dC = 0.4067

print(20.1*math.sqrt(273+25))
