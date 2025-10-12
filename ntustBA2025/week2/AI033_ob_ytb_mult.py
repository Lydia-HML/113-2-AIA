import cv2
import yt_dlp
import mediapipe as mp
import numpy as np

# 初始化 Mediapipe 物件偵測器
base_options = mp.tasks.BaseOptions('models/efficientdet_lite0.tflite')
options = mp.tasks.vision.ObjectDetectorOptions(base_options, score_threshold=0.2)
detector = mp.tasks.vision.ObjectDetector.create_from_options(options)


def get_youtube_stream_url(video_url):
    """ 獲取 YouTube 影片的串流 URL """
    ydl_opts = {'format': 'best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict['url']


# YouTube 影片網址
video_urls = [
    "https://www.youtube.com/watch?v=v9rQqa_VTEY",
    "https://www.youtube.com/watch?v=XUWjAsajKXg",
    "https://www.youtube.com/live/fP4ecxfsJos?si=jJpaVglyUoHB1OtQ",
    "https://www.youtube.com/live/z_fY1pj1VBw?si=PHZ1WcarxAEf_PTv"

]

# 取得串流 URL 並開啟影片
caps = [cv2.VideoCapture(get_youtube_stream_url(url)) for url in video_urls]

while all(cap.isOpened() for cap in caps):
    frames = []
    for cap in caps:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.resize(frame, (600, 360))
        image_mp = mp.Image(mp.ImageFormat.SRGB, frame)
        detection_result = detector.detect(image_mp)

        for detection in detection_result.detections:
            bbox = detection.bounding_box
            cv2.rectangle(frame, (bbox.origin_x, bbox.origin_y),
                          (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height), (100, 200, 0), 1)
            category = detection.categories[0]
            result_text = f"{category.category_name} ({round(category.score, 2)})"
            cv2.putText(frame, result_text, (10 + bbox.origin_x, 20 + bbox.origin_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        frames.append(frame)

    if len(frames) == len(caps):

        combined_frame = np.vstack(frames)
        row1 = np.hstack(frames[:2])
        row2 = np.hstack(frames[2:]) if len(frames) > 2 else None
        combined_frame = np.vstack([row1,row2]) if row2 is not None else row1
        # combined_frame = np.vstack(frames)  # 水平拼接兩個影片畫面
        cv2.imshow('Combined Videos', combined_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

for cap in caps:
    cap.release()
cv2.destroyAllWindows()