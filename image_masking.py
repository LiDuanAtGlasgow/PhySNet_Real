#pylint:skip-file
import os
import cv2
import glob

img_path='./renamed_images/'
mask_path='./masks/'
rgb_target='./masked_rgb/'
depth_target='./masked_depth/'
if not os.path.exists(rgb_target):
    os.makedirs(rgb_target)
if not os.path.exists(depth_target):
    os.makedirs(depth_target)

i=0
for fil in sorted(glob.glob(img_path+'*rgb.png'),key=str.lower):
    i+=1
    image=cv2.imread(fil)
    mask=cv2.imread(mask_path+str(i).zfill(4)+'_mask.png',0)
    image[mask>0]=0
    cv2.imwrite(rgb_target+str(i).zfill(4)+'.png',image)
i=0
for fil in sorted(glob.glob(img_path+'*depth.png'),key=str.lower):
    i+=1
    image=cv2.imread(fil,0)
    mask=cv2.imread(mask_path+str(i).zfill(4)+'_mask.png',0)
    mask_not=cv2.bitwise_not(mask)
    image=cv2.bitwise_and(image,mask_not)
    cv2.imwrite(depth_target+str(i).zfill(4)+'.png',image)
print('fil finish!')