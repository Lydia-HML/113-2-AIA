import cv2
import numpy as np
import mediapipe as mp

# 初始化 MediaPipe Face Mesh
mpd = mp.solutions.drawing_utils
mpfm = mp.solutions.face_mesh
dspec = mpd.DrawingSpec((0, 0, 0), 1, 1)
cspec = mpd.DrawingSpec((100, 100, 100), 1, 1)
cspec2 = mpd.DrawingSpec((224, 224, 224), 2, 2)
cpoint = mpfm.FACEMESH_TESSELATION
cpoint2 = mpfm.FACEMESH_CONTOURS
fm = mpfm.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 開啟攝影機
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    w, h = (int(image.shape[1]/2), int(image.shape[0]/2))
    # imagesBK = np.zeros([2, h, w, 3], np.uint8)
    imagesBK = np.zeros([2, h, w, 3], np.uint8)# 創建 2 張黑色影像
    imagesBK[:] = [255, 255, 255] # 讓整個陣列變成白色
    # imagesBK[0][:] = [255, 0, 0] # 設定第一張影像為藍色 (BGR: 255,0,0)
    # imagesBK[1][:] = [0, 255, 0] # 設定第二張影像為綠色 (BGR: 0,255,0)

    imgrgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = fm.process(imgrgb)                          # process the image
    if results.multi_face_landmarks:
        for f_landmarks in results.multi_face_landmarks:
            mpd.draw_landmarks(imagesBK[0], landmark_list=f_landmarks, connections=cpoint,
                               landmark_drawing_spec=dspec, connection_drawing_spec=cspec)
            mpd.draw_landmarks(imagesBK[1], landmark_list=f_landmarks, connections=cpoint2,
                               landmark_drawing_spec=dspec, connection_drawing_spec=cspec2)
    cv2.imshow('Lydia_faceLM2', np.hstack((imagesBK[0], cv2.flip(imagesBK[1], 1))))
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()