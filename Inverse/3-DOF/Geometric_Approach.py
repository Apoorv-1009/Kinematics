
#Geometrical Approach:

import math as m

x = 6
y = 8
z = 10
l1 = 10;
l2 = 10;
pi = 3.141592653589793;
d = x*x + y*y + z*z;

th = m.atan(x/y);
th = (180*th)/pi;

b = m.acos((l1*l1 + l2*l2 - d)/(2*l1*l2));
b = (180*b)/pi;
#print("b:",b); 
th2 = 180 - b;

a = m.atan((l2*m.sin(m.radians(th2)))/(l1+l2*m.cos(m.radians(th2))));
#print("a:",a);
th1 = m.atan((z)/(m.sqrt(x*x + y*y))) - a;
th1 = (180*th1)/pi;

print("th =",th);
print("th1 =",th1);
print("th2 =",th2);