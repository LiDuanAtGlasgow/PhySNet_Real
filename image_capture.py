#!/usr/bin/env python
#pylint:skip-file
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import message_filters
import time
import os
from PIL import Image as PIL_Image

img_path='./images/'
if not os.path.exists(img_path):
  os.makedirs(img_path)
def callback(rgb_msg,depth_msg):
  bridge=CvBridge()
  depth_img=bridge.imgmsg_to_cv2(depth_msg)
  rgb_img=bridge.imgmsg_to_cv2(rgb_msg,'bgr8')
  depth_array=np.array(depth_img,dtype=np.float32)
  cv2.normalize(depth_array,depth_array,0,1,cv2.NORM_MINMAX, dtype=cv2.CV_32F)
  cv2.imwrite(img_path+'%f_depth.png'%time.time(),depth_array*255)
  cv2.imwrite(img_path+'%f_rgb.png'%time.time(),rgb_img)


if __name__ == "__main__":
  depth_sub = message_filters.Subscriber('/camera/depth/image_raw',Image)
  rgb_sub=message_filters.Subscriber('/camera/rgb/image_raw',Image)
  ts=message_filters.ApproximateTimeSynchronizer([rgb_sub,depth_sub],10,0.1,allow_headerless=True)
  ts.registerCallback(callback)
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()
