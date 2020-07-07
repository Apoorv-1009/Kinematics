#Product Of Exponentials Approach:

import math as m
import numpy as np
import modern_robotics as mr


th = m.radians(0);   #rotation of shoulder about z axis;
th1 = m.radians(0);   #inclination of shoulder w.r.t xy plane
th2 = m.radians(0);   #inclination of link 1 w.r.t link 2
th3 = m.radians(0);   #rotation of link 3 about z axis of link 2
th4 = m.radians(0);   #inclination of link 3 w.r.t xy plane of link 2

l1 = 5;
l2 = 5;
l3 = 5;
h = 0;   #Height  of the Base above the Ground

l = l1+ l2 + l3
L = l1 + l2

M = np.array([[ 1 , 0 , 0 , l ],
              [ 0 , 1 , 0 , 0 ],
              [ 0 , 0 , 1 , h ],
              [ 0 , 0 , 0 , 1 ]])
#M

Slist = np.array([[ 0 , 0 , 1 , 0 , 0 , 0 ],     #S0
                  [ 0 ,-1 , 0 , h , 0 , 0 ],     #S1
                  [ 0 ,-1 , 0 , h , 0 ,-l1],     #S2
                  [ 0 ,-1 , 0 , h , 0 ,-L ],     #S3
                  [ 0 , 0 , 1 , 0 ,-L , 0 ]]).T  #S4
#Slist

thlist = np.array([th , th1 , th2 , th3 , th4]); 
#thlist

R = mr.FKinSpace(M,Slist,thlist)

for i in range(0,4):
    for j in range(0,4):
         R[i][j] = round(R[i][j])

R