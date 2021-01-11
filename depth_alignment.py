#pylint:skip-file
import os
import cv2
import numpy as np

real=cv2.imread('./real.png',0)
sim=cv2.imread('./simulation.png',0)
real=np.dot(real,0.75)
cv2.imwrite('./reduced_real.png',real)
real=np.asarray(real)
real=np.expand_dims(np.expand_dims(real,axis=0),axis=1)
print ('real:',real.shape)
sim=np.asarray(sim)
sim=np.expand_dims(np.expand_dims(sim,axis=0),axis=1)
print ('sim:',sim.shape)
mean=np.mean(real)
std=np.std(real)
print ('mean:',mean,'std0:',std)

