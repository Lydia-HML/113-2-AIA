import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #black background
cv2.imshow("Black Image",img)
print(img.shape)
img[:] = 255,0,0
img[200:300,100:300]=0,255,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
cv2.rectangle(img,(0,0),(255,350),(0,222,255),1)
cv2.circle(img,(400,150),50,(255,255,0),5)
cv2.putText(img," NTUST ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(100,220,222),2)
cv2.imshow("Lydia_AI024",img)
cv2.waitKey(0)
