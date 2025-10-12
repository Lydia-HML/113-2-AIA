import time
import streamlit as st
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCHED_DIR = "./data"  # 監控這個資料夾

class FileChangeHandler(FileSystemEventHandler):
    def on_
        modified(self, event):
        if event.src_path.endswith(".csv") or event.src_path.endswith(".json"):
            print(f"檔案變更偵測到: {event.src_path}")
            st.rerun()  # 強制 Streamlit 重新執行

def watch_files():
    observer = Observer()
    event_handler = FileChangeHandler()
    observer.schedule(event_handler, WATCHED_DIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# 在 Streamlit 內部執行監控
if __name__ == "__main__":
    watch_files()
