# pip install streamlit
# streamlit run AI101_st1.py
import cv2
import streamlit as st

cap = cv2.VideoCapture(0)

st.title('Streamlit + CV2')
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])

while run:
    success, frame = cap.read()
    FRAME_WINDOW.image(frame, channels= 'BGR')

cap.release()

# # Streamlit's logic
# if run:
#     st.write("Streaming...")
#     while run:
#         success, frame = cap.read()
#         if not success:
#             st.error("Unable to access the camera.")
#             break
#         FRAME_WINDOW.image(frame, channels='BGR')  # Display the frame
#         run = st.checkbox('Run')  # Keep updating the state of 'Run'
# else:
#     st.write("Click the 'Run' checkbox to start the webcam.")

# Release camera resource
# cap.release()
