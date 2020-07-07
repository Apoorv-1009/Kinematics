#Transformation Matrix Approach:
import math as m
import numpy as n


th = 0;   #rotation of shoulder about z axis;
th1 = 90;   #inclination of shoulder w.r.t xy plane
th2 = 0;   #inclination of link 1 w.r.t link 2
th3 = 0;   #rotation of link 3 about z axis of link 2
th4 = 0;   #inclination of link 3 w.r.t xy plane of link 2

l1 = 5;
l2 = 5;
l3 = 5;
h = 0;   #Height between Base and the Ground
h1 = 0;   
h2 = 0;   


#All Angles:
cth = m.cos(m.radians(th));
if(cth < 0.01): cth = 0;
sth = m.sin(m.radians(th));
if(sth < 0.01): sth = 0
cth1 = m.cos(m.radians(th1));
if(cth1 < 0.01): cth1 = 0;
sth1 = m.sin(m.radians(th1));
if(sth1 < 0.01): sth1 = 0;
cth2 = m.cos(m.radians(th2));
sth2 = m.sin(m.radians(th2));
cth3 = m.cos(m.radians(th3));
sth3 = m.sin(m.radians(th3));
cth4 = m.cos(m.radians(th4));
sth4 = m.sin(m.radians(th4));

#Transformation Of Shoulder(Rotation):
H01 = n.matrix([[cth,-1*sth,0,0],[sth,cth,0,0],[0,0,1,h],[0,0,0,1]]);
#print(H01);

#Transformation Of Shoulder(Inclination):
H12 = n.matrix([[cth1,0,-1*sth1,0],[0,1,0,0],[sth1,0,cth1,h1],[0,0,0,1]]);
#print(H12);

#Transformation Of link 2 w.r.t link 1:
H23 = n.matrix([[cth2,0,-1*sth2,l1],[0,1,0,0],[sth2,0,cth2,0],[0,0,0,1]]);
#print(H23);

#Transformation Of Link 2(Rotation):
H34 = n.matrix([[cth3,-1*sth3,0,l2],[sth3,cth3,0,0],[0,0,1,0],[0,0,0,1]]);
#print(H34);

#Transformation Of Link 2(Inclination):
H45 = n.matrix([[cth4,0,-1*sth4,0],[0,1,0,0],[sth4,0,cth4,h2],[0,0,0,1]]);
#print(H45);

#Position Of End Effector:
H56 = n.matrix([[l3],[0],[0],[1]]);
#print(56)

R = H01*H12*H23*H34*H45*H56;

print("R: \n", R);