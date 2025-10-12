import cv2
import numpy as np
import mediapipe as mp

selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(0)  # Using general mode (mode 0)
bgb = np.zeros([300,520,3], np.uint8)# 創建 300x520 的黑色背景；np.zeros() 代表全黑；np.uint8：像素值範圍 [0,255]
bgc = cv2.imread('../AI2015/pic/bgc.jpg')
cap = cv2.VideoCapture(0)   

while cap.isOpened():
    success, image = cap.read() #success指是否成功讀取影像 (True/False), image指讀取到的影像 (BGR 格式)
    img = cv2.resize(image,(520,300))
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = selfie_segmentation.process(imgrgb) #results.segmentation_mask (0 到 1 的灰階影像，數值越接近 1 代表越可能是前景)。
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.5
    output_image = np.where(condition, img, bgb) #[前景保留，背景變黑]. 如果 condition 為 True（即 segmentation_mask > 0.1），則選擇 img（原影像）
    output_image2 = np.where(condition, img, bgc)
    cv2.imshow('Lydia_original', img)
    cv2.imshow('Lydia_segmentation_black', output_image)
    cv2.imshow('Lydia_segmentation_color', output_image2)

    #cv2.waitKey(5)： 等待5ms，讓影像顯示。 當按下 ESC (27) 鍵時，跳出迴圈並結束程式。
    if cv2.waitKey(5)  & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()