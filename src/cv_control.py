import numpy as np
import cv2
import time
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt


def read_line(filein):
    img = cv2.imread(filein)
    image = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    lower = np.uint8([0,200,0])
    upper = np.uint8([255,255,255])
    white_mask = cv2.inRange(image,lower,upper)

    # add yellow color mask
    lower = np.uint8([10,0,100])
    upper = np.uint8([40,255,255])
    yellow_mask = cv2.inRange(image,lower,upper)

    # combine the results together
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    result = img.copy()
    cv2.imshow("mask",mask)



