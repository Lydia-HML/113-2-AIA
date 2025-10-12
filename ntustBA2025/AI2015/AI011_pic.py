import cv2

cap = cv2.VideoCapture('pic/cat_and_dog.jpg')
success, img = cap.read()
cv2.imshow('Lydia_AI011', img)
cv2.waitKey(0)