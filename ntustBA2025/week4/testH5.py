import tensorflow as tf
import os
import h5py

model_path = '../AI2015/models/keras_model.h5'

try:
    with h5py.File(model_path, 'r') as f:
        print("Valid .h5 file")
except OSError:
    raise ValueError("Invalid or corrupted .h5 file")


# Validate file existence
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Validate file format
try:
    with h5py.File(model_path, 'r') as f:
        print("Valid .h5 file")
except OSError:
    raise ValueError("Invalid or corrupted .h5 file")

# Load the model
try:
    model = tf.keras.models.load_model(model_path, compile=False)  # Assuming only inference is needed
except Exception as e:
    raise RuntimeError(f"Could not load the model: {e}")

print("Model loaded successfully!")
