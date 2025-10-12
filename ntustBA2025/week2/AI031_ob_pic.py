import cv2
import mediapipe as mp

base_options = mp.tasks.BaseOptions('models/efficientdet_lite0.tflite')　# 設定model 路徑
options = mp.tasks.vision.ObjectDetectorOptions(base_options, score_threshold=0.5) # 設定有 5成的信心，就可以秀出
detector = mp.tasks.vision.ObjectDetector.create_from_options(options)

cap = cv2.VideoCapture('../AI2015/pic/cat_and_dog.jpg')
success, image = cap.read()

image_mp = mp.Image(mp.ImageFormat.SRGB, image)  # prepare image for mediapipe
detection_result = detector.detect(image_mp)     # send image_mp to detector

for detection in detection_result.detections:
  bbox = detection.bounding_box
  cv2.rectangle(image, (bbox.origin_x, bbox.origin_y),
                (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height), (0, 0, 255), 2)
  category = detection.categories[0]
  result_text = category.category_name + ' (' + str(round(category.score, 2)) + ')'
  cv2.putText(image, result_text, (10 + bbox.origin_x, 20 + bbox.origin_y),
              1, 1, (0, 0, 255), 1)
cv2.imshow('Lydia_obj_pic', image)
cv2.waitKey(0)