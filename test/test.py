import cv2
import numpy as np

filename = './fingerprint_images/Avinash.png'
filename1 = './fingerprint_images/Avinasha.png'
img = cv2.imread(filename)
img1 = cv2.imread(filename1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
gray1 = np.float32(gray1)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst1 = cv2.cornerHarris(gray1,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
dst1 = cv2.dilate(dst1,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
img1[dst1>0.01*dst1.max()]=[0,0,255]

cv2.imshow('dst',img)
cv2.imshow('dst1',img1)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()