#pylint: skip-file
import os
import cv2
import glob
import numpy as np

img_path='./renamed_images/'
target_path='./masks/'
if not os.path.exists(target_path):
    os.makedirs(target_path)

i=0
for fil in sorted(glob.glob(img_path+'*rgb.png'),key=str.lower):
    i+=1
    image=cv2.imread(fil)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    blue_lower=np.array([30,40,40],np.uint8)
    blue_upper=np.array([71,255,255],np.uint8)
    mask=cv2.inRange(hsv,blue_lower,blue_upper)
    #lower_bound=np.array([44,54,63],np.uint8)
    #upper_bound=np.array([71,255,255],np.uint8)
    cv2.imwrite(target_path+str(i).zfill(4)+'_mask.png',mask)
print ('finished!')