#Transformation Matrix Approach:
import math 

l1 = 5;
l2 = 5;
th1 = 90;   #inclination of link 1 w.r.t x-axis
th2 = -90;   #inclination of link 2 w.r.t link 1

x1 = l2*math.cos(math.radians(th2));
y1 = l2*math.sin(math.radians(th2));

X = x1*math.cos(math.radians(th1)) - y1*math.sin(math.radians(th1));
Y = x1*math.sin(math.radians(th1)) + y1*math.cos(math.radians(th1));

x = X + l1*math.cos(math.radians(th1));
y = Y + l1*math.sin(math.radians(th1));
if(abs(x)<0.1):
    x = 0;
if(abs(y)<0.1):
    y = 0;
print(x);
print(y);