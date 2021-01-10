#pylint:skip-file
import os
import cv2
import numpy as np

image=cv2.imread('./result.png',0)
image_reduced=image/3
cv2.imwrite('./image_reduced.png',image_reduced)
depth_simulate=cv2.imread('./depth_simulate.png',0)
mask=cv2.imread('./mask.png',0)
mask=cv2.bitwise_not(mask)
result=cv2.bitwise_and(image,mask)
depth_simulate=np.asarray(depth_simulate)
depth_simulate=np.expand_dims(np.expand_dims(depth_simulate,axis=0),axis=1)
image_reduced=np.asarray(image_reduced)
image_reduced=np.expand_dims(np.expand_dims(image_reduced,axis=0),axis=1)
print (image_reduced.shape)
mean=np.mean(image_reduced,axis=(0,2,3))
std0=np.std(image_reduced,axis=(0,2,3))
std1=np.std(image_reduced,axis=(0,2,3),ddof=1)
print ('mean:',mean,'std0:',std0,'std1:',std1)

