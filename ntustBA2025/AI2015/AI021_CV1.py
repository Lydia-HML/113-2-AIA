import cv2
# cap = cv2.VideoCapture("video/RICH3.mp4")
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=13380")
while cap.isOpened():
    success, frame = cap.read()
    cv2.imshow("11302AIA_Lydia", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
