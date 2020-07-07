#Geometric Approach:

import math as m

x = 5
y = 15
l1 = 10;
l2 = 10;
pi = 3.141592653589793;
d = x*x+y*y;
a = m.acos((l1*l1 + l2*l2 - d)/(2*l1*l2));
a = (180*a)/pi;
th2 = 180 - a;
#print("a:",a);

b = m.atan((l2*m.sin(m.radians(th2)))/(l1+l2*m.cos(m.radians(th2))));
th1 = m.atan(y/x) - b;
th1 = (180*th1)/pi;
#print("b:",b);

if(abs(th1)<0.5):
    th1 = 0;
if(abs(th2)<0.5):
    th2 = 0;
print("th1:",round(th1));
print("th2:",round(th2));
