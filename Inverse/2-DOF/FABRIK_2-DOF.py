import math as m
from math import radians as r
import modern_robotics as mr
import numpy as np
from numpy import linalg as LA

def Angle_Calc(J , C):
    th1 = m.atan2(J[1],J[0])
    th1 = Degree_Conv(th1)
    #print("th1 =",th1)
    a = m.atan2(C[1] - J[1],C[0] - J[0])
    a = Degree_Conv(a)
    #print(a)
    th2 = a - th1
    #print("th2 =",th2)
    thu = th_update(th1,th2)
    return thu

def Degree_Conv(x):
    pi = m.pi
    x = (x/pi)*180
    return x

def th_update(th1, th2):
    th = np.array([th1 , th2])
    return th

def Ef_Solver(th):
    Ef = np.array([[ l1*m.cos(r(th[0])) + l2*m.cos(r(th[0]+th[1])) ],   #End-Effector Position /J2
                   [ l1*m.sin(r(th[0])) + l2*m.sin(r(th[0]+th[1])) ]])
    print("End Effector currently at:\n ",Ef)

def J1_Solver(th):
    J1 = np.array([[ l1*m.cos(r(th[0])) ],   #Joint 1 Position
                   [ l1*m.sin(r(th[0])) ]])
    #print("Joint 1 Currently at: \n",J1)
    return J1

#Initialize:
Ef_d = np.array([[4 , 4]]).T   #The End-Effector Desired Position: [x , y]
P = np.array([0 , 0]).T   #The End-Effector Current Position: [x , y]
th = th_update(0,0)   #Initial Joint Angles
O = np.array([[ 0 , 0]]).T
err_x = 0.0001
err_y = 0.0001
l1 = 5   #Link 1 Length
l2 = 5   #Link 2 Length

i = 0
e = True   #Error Initially True
while i < 10 and e :
    print("Iteration:",i+1)

    J1 = J1_Solver(th)
    #print(J1-Ef_d)
    UntVec_1 = mr.Normalize(J1 - Ef_d)
    #print(UntVec_1)
    J1n = np.dot(l2,UntVec_1) + Ef_d   #J1n is the pseudo Joint 1 Position
    #print(J1n,"\n \n")

    UntVec_2 = mr.Normalize(J1n - O)
    J1nn = np.dot(l1,UntVec_2) 
    print("J1 Current Position: \n",J1nn,"\n ")   #J1nn is the updated Position of Joint 1

    UntVec_3 = mr.Normalize(Ef_d - J1nn)
    P = np.dot(l2,UntVec_3) + J1nn
    print("Current End-Effector Position: \n",P,"\n ")   #P is the updated Position of the End-Effector

    th = Angle_Calc(J1nn,P)
    print("Current Th list:",th)
    e = abs(P[0] - Ef_d[0]) > err_x or abs(P[1] - Ef_d[1]) > err_y
    print("\n \n")
    i = i + 1

print("th1 =",th[0])
print("th2 =",th[1])
Ef_Solver(th)