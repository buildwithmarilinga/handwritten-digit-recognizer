# ✍️ Handwritten Digit Recognizer (MNIST - CNN)

This project is a Deep Learning application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset.

---

## 🚀 Features

- Upload handwritten digit image
- Predict digit (0–9)
- High accuracy (~99%)
- Simple and interactive UI using Streamlit

---

## 🧠 Model Details

- Algorithm: Convolutional Neural Network (CNN)
- Dataset: MNIST
- Accuracy: ~99%
- Framework: TensorFlow / Keras

---

## 🛠️ Tech Stack

- Python  
- TensorFlow / Keras  
- NumPy  
- Streamlit  
- PIL (Image Processing)

---

## 📂 Project Structure

digit-recognizer/

│
├── train.py # Model training

├── predict.py # Prediction logic

├── streamlit_app.py # Web app

├── requirements.txt # Dependencies

│
├── models/

│ └── digit_model.h5 # Trained model

│

├── test_images/ # Sample images


---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt

2️⃣ Train the model
python train.py

3️⃣ Run the application
streamlit run streamlit_app.py

4️⃣ Open in browser
http://localhost:8501
