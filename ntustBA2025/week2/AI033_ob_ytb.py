import cv2
import yt_dlp
import mediapipe as mp

base_options = mp.tasks.BaseOptions('models/efficientdet_lite0.tflite')
options = mp.tasks.vision.ObjectDetectorOptions(base_options, score_threshold=0.2)
detector = mp.tasks.vision.ObjectDetector.create_from_options(options)

# video_url = "https://www.youtube.com/watch?v=v9rQqa_VTEY"
# video_url = "https://www.youtube.com/watch?v=XUWjAsajKXg"
# video_url = "https://www.youtube.com/live/z_fY1pj1VBw?si=PHZ1WcarxAEf_PTv"
video_url = "https://www.youtube.com/live/fP4ecxfsJos?si=jJpaVglyUoHB1OtQ"
video_url2 = "https://www.youtube.com/watch?v=5u4xTa3LR2U"

ydl_opts = {'format': 'best',  'quiet': True }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
stream_url = info_dict['url']

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url2, download=False)
stream_url2 = info_dict['url']


cap = cv2.VideoCapture(stream_url)
cap2 = cv2.VideoCapture(stream_url2)


while cap.isOpened():
    success, image = cap.read()
    success, image2 = cap2.read()
    image = cv2.resize(image, (600, 360))
    image2 = cv2.resize(image2, (600, 360))
    image_mp = mp.Image(mp.ImageFormat.SRGB, image)  # prepare image for mediapipe
    image_mp2 = mp.Image(mp.ImageFormat.SRGB, image2)  # prepare image for mediapipe
    detection_result = detector.detect(image_mp)  # send image_mp to detector
    detection_result2 = detector.detect(image_mp)  # send image_mp to detector

    for detection in detection_result.detections:
      bbox = detection.bounding_box
      cv2.rectangle(image, (bbox.origin_x, bbox.origin_y),
                    (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height), (100, 200, 0), 1)
      category = detection.categories[0]
      result_text = category.category_name + ' (' + str(round(category.score, 2)) + ')'
      cv2.putText(image, result_text, (10 + bbox.origin_x, 20 + bbox.origin_y),
                  1, 1, (255, 255, 255), 1)
    cv2.imshow('Lydia_obj_ytb', image)

    for detection in detection_result2.detections:
      bbox = detection.bounding_box
      cv2.rectangle(image2, (bbox.origin_x, bbox.origin_y),
                    (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height), (100, 200, 0), 1)
      category = detection.categories[0]
      result_text = category.category_name + ' (' + str(round(category.score, 2)) + ')'
      cv2.putText(image2, result_text, (10 + bbox.origin_x, 20 + bbox.origin_y),
                  1, 1, (255, 255, 255), 1)
    cv2.imshow('Lydia_obj_ytb_2', image2)

    if cv2.waitKey(1) & 0xFF == 27:
       break

cap.release()
cv2.destroyAllWindows()