#Geometric Approach:

import math
l1 = 10;
l2 = 10;
th1 = 0;   #th1 gives elevation of shoulder
th = -90;  #th gives rotation to shoulder
thr = 0;   #thr gives the joint 1 angle 
th4 = 180 - thr;
x = (l1*cos(math.radians(th1)) + l2*sin(math.radians(th4 + th1 - 90)))*cos(math.radians(th));
y = (l1*cos(math.radians(th1)) + l2*sin(math.radians(th4 + th1 - 90)))*sin(math.radians(th));
z = l1*sin(math.radians(th1)) - l2*cos(math.radians(th4 + th1 - 90));
if(abs(x)<0.5):
    x = 0;
if(abs(y)<0.5):
    y = 0;
if(abs(z)<0.5):
    z = 0;
print("x:",x);
print("y:",y);
print("z:",z);