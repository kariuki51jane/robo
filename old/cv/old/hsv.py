import cv2
import numpy as np

green = np.uint8([[[220,211,211 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
