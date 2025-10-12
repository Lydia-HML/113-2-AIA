import cv2
img = cv2.imread("pic/cat_and_dog.jpg")
img = cv2.resize(img,(800,480))
imgCropped = img[210:460, 160:360]
# crop_image = image[x:x+w, y:y+h]
print(img.shape)
print(imgCropped.shape)
cv2.imshow("Lydia_AI023",img)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)
