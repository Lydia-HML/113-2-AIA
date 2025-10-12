import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('../AI2015/models/keras_model.h5', compile=False) # Load the model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)   # Create the array to feed into the keras model

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    img = cv2.resize(image , (224, 224))    # resizing the image to 224x224
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)
    image_array = np.asarray(img)                # turn the image into a numpy array
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image_array             # Load the image into the array
    prediction = model.predict(data)             # Predicts the model
    a,b,c = prediction[0]
    if a>0.5:
        print('Give me 5!')
        cv2.putText(image, 'Give me 5!', (530, 120), 1, 5, (255,0, 255), 10, 1)
    if b>0.3:
        print('No sign ')
        cv2.putText(image, 'No sign ', (30, 120), 1, 5, ( 255,0,0), 10,1)
    if c>0.4:
        print('Zero!')
        cv2.putText(image, 'Zero!', (330, 120),1, 5, (0, 0, 255), 10, 1)
    cv2.putText(image, 'Zero!:'+ str(c), (30, 220),1, 2, (0, 0, 255), 1, 1)
    cv2.putText(image, 'No sign  :' + str(b), (30, 260), 1, 2, (255,0,0), 1, 1)
    cv2.putText(image, 'Give me 5! :'+ str(a), (30, 300), 1, 2, (255, 0, 255), 1, 1)
    cv2.imshow('Lydia_gesture3', image)
    if cv2.waitKey(500) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()