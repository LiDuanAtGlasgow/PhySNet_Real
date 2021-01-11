#pylint:skip-file
import os
import cv2
import glob
import numpy as np

target_path='./aligned_depth/'
if not os.path.exists(target_path):
    os.makedirs(target_path)
i=0
for fil in sorted(glob.glob('./masked_depth/*'),key=str.lower):
    image=cv2.imread(fil,0)
    i+=1
    image_reduced=np.dot(image,0.75)
    cv2.imwrite(target_path+str(i).zfill(4)+'.png',image_reduced)
print('alignings finished!')