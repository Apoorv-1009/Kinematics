#Transformation Matrix Approach:

import math as m
import numpy as n

th = 0;   #inclination of shoulder w.r.t xy plane
th1 = 0;   #rotation of shoulder about z axis
th2 = 0;   #inclination of link 2 w.r.t link 1 

l1 = 0;
l2 = 5;
l3 = 5;
h = 0;

#All Angles:
cth = m.cos(m.radians(th));
if(abs(cth)<0.0001): cth = 0;
sth = m.sin(m.radians(th));
if(abs(sth)<0.0001): sth = 0;
cth1 = m.cos(m.radians(th1));
if(abs(cth1)<0.0001): cth1 = 0;
sth1 = m.sin(m.radians(th1));
if(abs(sth1)<0.0001): sth1 = 0;
cth2 = m.cos(m.radians(th2));
if(abs(cth2)<0.0001): cth2 = 0;
sth2 = m.sin(m.radians(th2));
if(abs(sth2)<0.0001): sth2 = 0;

#Base to Link 1 (Rotation Of Shoulder):
H01 = n.matrix([[cth,-1*sth,0,0],[sth,cth,0,0],[0,0,1,h],[0,0,0,1]]);
#print(H01);

#Link 1 to Link 2 (Elevation Of Shoulder):
H12 = n.matrix([[cth1,0,-1*sth1,0],[0,1,0,0],[sth1,0,cth1,l1],[0,0,0,1]]);
#print(H12);

#Link 2 to Link 3 (Elevation of Link):
H23 = n.matrix([[cth2,0,-1*sth2,l2],[0,1,0,0],[sth2,0,cth2,0],[0,0,0,1]]);
#print(H23);

#Link 3 to End-Effector:
#H34 = n.matrix([[1,0,0,l3],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
H34 = n.matrix([[l3],[0],[0],[1]]);


#print(P);
R = (H01*H12*H23*H34);
print("R: \n",R);
