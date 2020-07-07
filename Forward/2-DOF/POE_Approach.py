#Product Of Exponentials Approach:

import numpy as np 
import modern_robotics as mr 
import math as m

l1 = 5   #Link 1 Length
l2 = 5   #Link 2 Length
l = l1+l2
th1 = m.radians(45)   # inclination of link 1
th2 = m.radians(0)   # inclination of link 2
print(th1)
M = np.array ([[ 1 , 0 , 0 , l ],
               [ 0 , 1 , 0 , 0 ],
               [ 0 , 0 , 1 , 0 ],
               [ 0 , 0 , 0 , 1 ]])
#M

Slist = np.array([[ 0 , 0 , 1 , 0 ,  0    , 0 ],
                  [ 0 , 0 , 1 , 0 , -1*l1 , 0 ]]).T

#Slist

thlist = np.array([ th1 , th2 ])
#thlist

R = np.round(mr.FKinSpace(M,Slist,thlist), decimals = 2)
R