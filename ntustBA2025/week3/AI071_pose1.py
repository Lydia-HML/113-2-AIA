import cv2
import mediapipe as mp

conn = mp.solutions.pose.POSE_CONNECTIONS
pose = mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mpd = mp.solutions.drawing_utils
spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    imgrgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(imgrgb)
    if results.pose_landmarks:
        mpd.draw_landmarks(image, results.pose_landmarks, conn, spec)
    cv2.imshow('Lydia_pose1', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()