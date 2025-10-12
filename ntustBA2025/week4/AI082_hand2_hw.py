import cv2
import mediapipe as mp
import random

mpd = mp.solutions.drawing_utils
lm_style = mp.solutions.drawing_styles.get_default_hand_landmarks_style()
conn_style = mp.solutions.drawing_styles.get_default_hand_connections_style()
mphc = mp.solutions.hands.HAND_CONNECTIONS
hands = mp.solutions.hands.Hands(model_complexity=0, max_num_hands=2)

cap = cv2.VideoCapture(0)
run = True
count = 0

while cap.isOpened():
    success, image = cap.read()
    img = cv2.resize(image, (640, 420))  # resize image
    w, h = (img.shape[1], img.shape[0])
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if run:
        run = False  # If it doesn't touch, it will remain 'False' (no position change)
        rx = random.randint(10, w - 80)  # Random x-coordinate
        ry = random.randint(10, h - 80) # Random y-coordinate
        box_randrbg = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
        count += 1
        print("New box:",rx, ry)
    results = hands.process(imgrgb)
    if results.multi_hand_landmarks:
        for h_landmarks in results.multi_hand_landmarks:
            mpd.draw_landmarks(img, h_landmarks, mphc, lm_style, conn_style)
            x = h_landmarks.landmark[8].x * w  # Get the x-coordinate of the index finger's tip
            y = h_landmarks.landmark[8].y * h  # Get the y-coordinate of the index finger's tip
            print(x, y)
            if x > rx and x < (rx + 80) and y > ry and y < (ry + 80):
                run = True
    randint = random.randint(0, 255)
    cv2.rectangle(img, (rx, ry), (rx + 80, ry + 80), box_randrbg, 5) # Draw the touch zone

    flipped_img = cv2.flip(img, 1)
    cv2.putText(flipped_img, "Socre : " + str(count), (100, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow('Lydia_hand2', flipped_img )

    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()