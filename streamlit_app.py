import streamlit as st
import numpy as np
from tensorflow import keras
from PIL import Image

st.title("✍️ Handwritten Digit Recognizer")

# Load model
try:
    model = keras.models.load_model("models/digit_model.h5")
    st.success("Model loaded successfully!")
except:
    st.error("Model not found! Run train.py first.")

# Upload image
uploaded_file = st.file_uploader("Upload a digit image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("L")
    img = img.resize((28, 28))

    st.image(img, caption="Uploaded Image")

    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    digit = np.argmax(prediction)

    st.success(f"Predicted Digit: {digit}")