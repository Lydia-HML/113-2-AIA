# yt-dlp 解析 YouTube 影片

import yt_dlp
import cv2

# video_url = "https://www.youtube.com/watch?v=Ilh29a8dzgQ"
# video_url = "https://youtu.be/5u4xTa3LR2U?si=Xx_TSHZ_gkTvf3gM"
video_url = "https://www.youtube.com/watch?v=5u4xTa3LR2U"
ydl_opts = {'format': 'best',  'quiet': True }
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
stream_url = info_dict['url']

cap = cv2.VideoCapture(stream_url)
# cap = cv2.VideoCapture(stream_url, cv2.CAP_FFMPEG)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (960, 540))
    cv2.imshow('Lydia_AI013', frame)
    if cv2.waitKey(1) & 0xFF == 27: # 按 'esc' 退出
        break
cap.release()
cv2.destroyAllWindows()
