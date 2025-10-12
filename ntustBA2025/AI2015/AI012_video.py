# Function: opencv VideoCapture
import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    cv2.imshow('Lydia_AI012', image)
    if cv2.waitKey(1) & 0xFF == 27:
       break
cap.release()
cv2.destroyAllWindows()
