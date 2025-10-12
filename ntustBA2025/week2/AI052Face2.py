import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection                          # setup face detection
mp_drawing = mp.solutions.drawing_utils                                  # setup drawing utils
face_detection= mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    imgrgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(imgrgb)
    w, h = (image.shape[1], image.shape[0])
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
            s = detection.location_data.relative_bounding_box             # get face bounding box
            eye = int(s.width * w * 0.1)                                  # eye size = 1/10 facesize
            a = detection.location_data.relative_keypoints[0]             # left eye
            b = detection.location_data.relative_keypoints[1]             # right eye
            c = detection.location_data.relative_keypoints[3]             # mouse
            d = detection.location_data.relative_keypoints[2]             # nose
            ax, ay = int(a.x * w), int(a.y * h)                           # real value
            bx, by = int(b.x * w), int(b.y * h)
            cx, cy = int(c.x * w), int(c.y * h)
            dx, dy = int(d.x * w), int(d.y * h)
            cv2.circle(image, (ax, ay), (eye + 10), (255, 255, 255), -1)  # draw left eye (white)
            cv2.circle(image, (bx, by), (eye + 10), (255, 255, 0), -1)    # draw right eye (white)
            cv2.circle(image, (ax, ay), eye, (0, 0, 0), -1)               # draw left eye (black)
            cv2.circle(image, (bx, by), eye, (0, 0, 0), -1)               # draw right eye (black)
            cv2.rectangle(image, (cx, cy), (cx+100, cy+100), (0, 0, 0), 10)
            cv2.circle(image, (dx, dy), 10, (0, 0, 0), -1)

    cv2.imshow('Lydia_face2', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()