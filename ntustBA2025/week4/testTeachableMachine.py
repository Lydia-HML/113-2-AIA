from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import tensorflow as tf
import cv2


model = tf.keras.models.load_model('models/keras_model.h5', compile=False) # Load the model
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
    a,b,c,d = prediction[0]                      # predict the class

    if a>0.5:
        print('Mug')
        cv2.putText(image, 'Mug', (530, 120), 1, 5, (255,0, 255), 10, 1)
    if b>0.5:
        print('Tiger ')
        cv2.putText(image, 'Tiger', (30, 120), 1, 5, ( 255,0,0), 10,1)
    if c>0.5:
        print('iPhone')
        cv2.putText(image, 'iPhone!', (330, 120),1, 5, (0, 0, 255), 10, 1)
    if d>0.5:
        print('Nothing')
        cv2.putText(image, 'Nothing!', (330, 120),1, 5, (0, 0, 255), 10, 1)
    cv2.putText(image, 'Mug:'+ str(a), (30, 220),1, 2, (0, 0, 255), 1, 1)
    cv2.putText(image, 'Tiger  :' + str(b), (30, 260), 1, 2, (255,0,0), 1, 1)
    cv2.putText(image, 'iPhone :'+ str(c), (30, 300), 1, 2, (255, 0, 255), 1, 1)
    cv2.putText(image, 'Nothing :' + str(d), (30, 300), 1, 2, (255, 0, 255), 1, 1)
    cv2.imshow('Lydia_gesture3', image)
    if cv2.waitKey(500) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()


# #############################
#
# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)
#
# # Load the model
# model = load_model("models/keras_Model.h5", compile=False)
#
# # Load the labels
# class_names = open("models/labels.txt", "r").readlines()
#
# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#
# # Replace this with the path to your image
# image = Image.open("../AI2015/pic/1.png").convert("RGB")
#
# # resizing the image to be at least 224x224 and then cropping from the center
# size = (224, 224)
# image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
#
# # turn the image into a numpy array
# image_array = np.asarray(image)
#
# # Normalize the image
# normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
#
# # Load the image into the array
# data[0] = normalized_image_array
#
# # Predicts the model
# prediction = model.predict(data)
# index = np.argmax(prediction)
# class_name = class_names[index]
# confidence_score = prediction[0][index]
#
# # Print prediction and confidence score
# print("Class:", class_name[2:], end="")
# print("Confidence Score:", confidence_score)
