# pip install streamlit
# streamlit run AI102_st2.py
import os
import cv2
import numpy as np
import streamlit as st
import yt_dlp
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ---------- Streamlit 基本設定 ----------
st.set_page_config(page_title="YouTube Object Detection (Ollama-ready)", layout="wide")
st.title("Streamlit + OpenCV + MediaPipe Object Detection")

# ---------- 參數 ----------
DEFAULT_URL = "https://www.youtube.com/watch?v=XUWjAsajKXg"
MODEL_PATH = "/Users/hmlin/PycharmProjects/ntustBA2025/AI2015/models/efficientdet_lite0.tflite"   # 確認路徑存在，或自行放到專案根目錄

# ---------- 工具函式 ----------
@st.cache_data(show_spinner=False)
def get_stream_url(youtube_url: str) -> str:
    ydl_opts = {"format": "best", "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
    return info["url"]

def ensure_model(path: str):
    if not os.path.exists(path):
        st.error(f"找不到模型檔：{path}。請下載 MediaPipe 的 efficientdet_lite0.tflite 並放到此路徑。")
        st.stop()

# ---------- 準備模型 ----------
ensure_model(MODEL_PATH)
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
detector_options = vision.ObjectDetectorOptions(
    base_options=base_options,
    score_threshold=0.2,
    max_results=5
)
detector = vision.ObjectDetector.create_from_options(detector_options)

# ---------- UI ----------
url = st.text_input("YouTube 連結", value=DEFAULT_URL)
col1, col2 = st.columns([1, 2])
with col1:
    run = st.toggle("Run", value=False)
    target_w = st.slider("寬度 (px)", 480, 1280, 960, step=40)
    show_score = st.checkbox("顯示信心分數", value=True)
with col2:
    frame_window = st.empty()

# ---------- 主流程 ----------
if run:
    stream_url = get_stream_url(url)
    cap = cv2.VideoCapture(stream_url, cv2.CAP_FFMPEG)  # 需要系統有 ffmpeg
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        st.error("無法開啟串流，請確認 ffmpeg 安裝或嘗試其他影片。")
        st.stop()

    try:
        while True:
            ok, frame_bgr = cap.read()
            if not ok or frame_bgr is None:
                st.warning("讀取串流失敗或已結束。")
                break

            # Resize
            h, w = frame_bgr.shape[:2]
            scale = target_w / float(w)
            frame_bgr = cv2.resize(frame_bgr, (int(w * scale), int(h * scale)))

            # OpenCV(BGR) -> MediaPipe(RGB)
            frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

            # 建立 MediaPipe Image
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

            # 偵測
            result = detector.detect(mp_image)

            # 繪製結果（畫在 BGR 畫布上）
            if result and result.detections:
                for det in result.detections:
                    bbox = det.bounding_box
                    x, y, w, h = int(bbox.origin_x), int(bbox.origin_y), int(bbox.width), int(bbox.height)
                    cv2.rectangle(frame_bgr, (x, y), (x + w, y + h), (100, 200, 0), 2)

                    if det.categories:
                        cat = det.categories[0]
                        label = cat.category_name or "obj"
                        if show_score and cat.score is not None:
                            label = f"{label} ({cat.score:.2f})"
                        cv2.putText(frame_bgr, label, (x + 6, max(20, y - 6)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

            # 顯示在 Streamlit
            frame_window.image(frame_bgr, channels="BGR")

            # 讓 Streamlit 有機會處理 UI 事件
            if not st.session_state.get("_run_flag", True):
                break

            # 如果使用者把 toggle 關掉，跳出
            if not st.session_state.get('run', run):
                break

            # 這行讓腳本每次迴圈後能「重新渲染」並檢查 UI 變化
            run = st.session_state.get('run', run)

    finally:
        cap.release()
else:
    st.info("⬆️ 輸入 YouTube 連結、打開『Run』就會即時推論啦。")
