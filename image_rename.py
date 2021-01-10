#pylint: skip-file
import os
import cv2
import glob

img_path='./selected_images/'
target_path='./renamed_images/'
if not os.path.exists(target_path):
    os.makedirs(target_path)

i=0
for fil in sorted(glob.glob(img_path+'*rgb.png'),key=str.lower):
    i+=1
    image=cv2.imread(fil)
    cv2.imwrite(target_path+str(i).zfill(4)+'_rgb.png',image)
print('files finished')