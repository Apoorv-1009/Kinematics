#Geometric Approach:

import math as m
l1 = 5;
l2 = 5;
th1 = 36;   #th1 is the elevation to the link1
th2 = 72;   #thr is the angle between link1 and link2

x = l1*m.cos(m.radians(th1)) + l2*m.cos(m.radians(th1+th2));
y = l1*m.sin(m.radians(th1)) + l2*m.sin(m.radians(th1+th2));

if(abs(x) < 0.5): x = 0;
if(abs(y) < 0.5): y = 0;
print("x =",round(x));
print("y =",round(y));