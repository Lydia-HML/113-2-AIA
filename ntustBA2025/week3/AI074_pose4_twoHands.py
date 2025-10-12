#https://storage.googleapis.com/mediapipe-assets/documentation/mediapipe_face_landmark_fullsize.png

import cv2 #cv2：用於讀取影像並顯示結果
import mediapipe as mp #mediapipe (mp)：Google 的人體姿勢偵測模型 MediaPipe Pose
import numpy as np #numpy (np)：用於數學運算，如插值 (interp)
import math  #math：用於計算角度 (math.atan2 和 math.degrees)


pose = mp.solutions.pose.Pose() #建立 Pose 偵測器，用來偵測人體關鍵點。
conn = mp.solutions.pose.POSE_CONNECTIONS #MediaPipe 預設的骨架連線
mpd = mp.solutions.drawing_utils #用來繪製人體關鍵點
spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style() #預設的姿勢點樣式

# 初始化變數
# switch : 偵測 手臂彎曲是否達到最低點（switch=1 代表曾達最低）
# count：計算 手臂完整舉起與放下的次數
# color：用來顯示條狀圖的顏色（紅色 (0,0,255) 代表還沒達到運動目標）
switch_right, count_right = 0, 0
switch_left, count_left = 0, 0
color_right = (0, 0, 255)
color_left = (0, 0, 255)

def is_valid_point(x, y, w, h):
    return 0 <= x < w and 0 <= y < h  # 確保點在畫面範圍內

#開啟攝影機
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read() #讀取攝影機影像
    imgrgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #轉換影像格式，以便 MediaPipe 偵測

    #進行姿勢偵測
    results = pose.process(imgrgb)  #用 MediaPipe Pose 偵測人體關鍵點
    h, w, c = image.shape #取得影像尺寸

    xx1 = int(w * 0.1)
    xx2 = int(w * 0.9)
    poslist = []

    if results.pose_landmarks:
        mpd.draw_landmarks(image, results.pose_landmarks, conn, spec)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            poslist.append([id, cx, cy])
    try:
        if len(poslist) > 16 :
            # The angle of the right
            x1, y1 = poslist[12][1], poslist[12][2]  # 右肩 (right_shoulder)
            x2, y2 = poslist[14][1], poslist[14][2]  # 右肘 (right_elbow)
            x3, y3 = poslist[16][1], poslist[16][2]  # 右手腕 (right_wrist)
            right_angle = abs(int(math.degrees(math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2))))

            # The angle of the left
            x4, y4 = poslist[11][1], poslist[11][2]
            x5, y5 = poslist[13][1], poslist[13][2]
            x6, y6 = poslist[15][1], poslist[15][2]
            left_angle = abs(int(math.degrees(math.atan2(y4 - y5, x4 - x5) - math.atan2(y6 - y5, x6 - x5))))

            # 繪製右手肘骨架
            if is_valid_point(x1, y1, w, h) and is_valid_point(x2, y2, w, h) and is_valid_point(x3, y3, w, h):
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 3)
                cv2.line(image, (x3, y3), (x2, y2), (0, 255, 255), 3)
                cv2.circle(image, (x1, y1), 10, (0, 255, 255), cv2.FILLED)
                cv2.circle(image, (x1, y1), 15, (0, 255, 255), 2)
                cv2.circle(image, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(image, (x2, y2), 15, (0, 0, 255), 2)
                cv2.circle(image, (x3, y3), 10, (0, 255, 255), cv2.FILLED)
                cv2.circle(image, (x3, y3), 15, (0, 255, 255), 2)

            # 繪製左手肘骨架
            if is_valid_point(x4, y4, w, h) and is_valid_point(x5, y5, w, h) and is_valid_point(x6, y6, w, h):
                cv2.line(image, (x4, y4), (x5, y5), (0, 255, 255), 3)
                cv2.line(image, (x6, y6), (x5, y5), (0, 255, 255), 3)
                cv2.circle(image, (x4, y4), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(image, (x5, y5), 10, (255, 0, 255), cv2.FILLED)
                cv2.circle(image, (x6, y6), 10, (255, 0, 255), cv2.FILLED)


            # right hand bending on a scale of 10 to 170 degrees, maximum 100% and minimum 0%
            # np.interp() 用來將 right_angle 對應到進度條數值：
            # right_angle = 10° → 進度條 100%（完全彎曲）
            # right_angle = 170° → 進度條 0 %（完全伸直）

            right_per = np.interp(right_angle, (10, 170), (100, 0))

            # the height of the bar on the Y-axis based on the degree of right hand bending, 200~400
            right_bar = int(np.interp(right_angle, (10, 170), (200, 400)))

            # **計算左手運動進度 percentage 和 畫 BAR **
            left_per = np.interp(left_angle, (10, 170), (100, 0))
            left_bar = int(np.interp(left_angle, (10, 170), (200, 400)))

            # **顯示右手進度條**
            # rectangle represent the bar's height and also display the numerical value
            cv2.rectangle(image, (xx1, int(right_bar)), (xx1 + 30, 400), color_right, cv2.FILLED)
            cv2.putText(image, str(int(right_per)) + '%', (xx1 - 10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, color_right, 2)
            # **顯示左手進度條**
            cv2.rectangle(image, (xx2, int(left_bar)), (xx2 + 30, 400), color_left, cv2.FILLED)
            cv2.putText(image, str(int(left_per)) + '%', (xx2 - 50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, color_left, 2)


            # hand raise to 95% or lower to 5%, it is considered halfway
            # **計算右手次數**
            # 當手肘完全彎曲(right_per >= 95 %)，記錄半次(count += 0.5)。
            # 當手肘完全伸直(right_per <= 5 %)，記錄半次(count += 0.5)。
            # 完整的上下彎曲，會累積1次。

            color_right = (0, 0, 255)
            if right_per >= 95:
                color_right = (0, 255, 0)
                if switch_right == 0:
                    count_right += 0.5
                    switch_right = 1
            if right_per <= 5:
                color_right = (0, 255, 0)
                if switch_right == 1:
                    count_right += 0.5
                    switch_right = 0

            # **計算左手次數**
            color_left = (0, 0, 255)
            if left_per >= 95:
                color_left = (0, 255, 0)
                if switch_left == 0:
                    count_left += 0.5
                    switch_left = 1
            if left_per <= 5: #當左手放下 (left_per <= 5%)，進度條顏色變為綠色
                color_left = (0, 255, 0)
                if switch_left == 1:
                    count_left += 0.5
                    switch_left = 0

    except Exception as e:
        print("error: ", e)

    # 顯示運動次數
    cv2.putText(image, "Right: " + str(int(count_right)), (xx1 - 40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
    cv2.putText(image, "Left: " + str(int(count_left)), (xx2 - 80, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 6)

    cv2.imshow('Lydia_pose3', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()