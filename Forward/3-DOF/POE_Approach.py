#Product Of Exponentials Approach:

import math as m
import modern_robotics as mr
import numpy as np

h = 0   #Height of the base above the ground
l1 = 5   #Length of link 1
l2 = 5   #Length of Link 2

th = m.radians(80)   #Rotation of Arm about z-axis
th1 = m.radians(90)   #Inclination of Link 1 w.r.t xy plane
th2 = m.radians(0)   #Inclination of Link 2 w.r.t link 1

l = l1 + l2

M = np.array([[ 1 , 0 , 0 , l ],
              [ 0 , 1 , 0 , 0 ],
              [ 0 , 0 , 1 , h ],
              [ 0 , 0 , 0 , 1 ]])
#M

Slist = np.array([[ 0 , 0 , 1 , 0 , 0 , 0 ],     #S0
                  [ 0 ,-1 , 0 , h , 0 , 0 ],     #S1
                  [ 0 , 1 , 0 ,-h , 0 , l1]]).T  #S2
#Slist

thlist = np.array([th , th1 , th2])
#thlist

R = mr.FKinSpace(M,Slist,thlist)

for i in range(0,4):
    for j in range(0,4):
        R[i][j] = round(R[i][j])
R
