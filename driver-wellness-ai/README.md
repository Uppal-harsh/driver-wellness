# 🚗 Driver Wellness AI

Driver Wellness AI is a real-time drowsiness detection system built using Python, computer vision, and facial landmark analysis. It continuously monitors a driver’s eye activity through a webcam and triggers alerts when signs of fatigue are detected.

---

## 🔍 Overview

Driver fatigue is a major cause of road accidents. This project aims to reduce that risk by:

* Tracking facial landmarks in real time
* Calculating Eye Aspect Ratio (EAR)
* Detecting prolonged eye closure (drowsiness)
* Triggering visual alerts to warn the driver

---

## ✨ Features

* 👁️ Real-time face and eye detection using OpenCV and dlib
* 📊 Eye Aspect Ratio (EAR)–based drowsiness detection
* ⚠️ Instant visual alert overlay when drowsiness is detected
* ⚡ Lightweight and runs on standard webcams
* 🧠 Modular code structure for easy expansion

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd driver-wellness-ai
```

---

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
.\venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download Facial Landmark Model

* Download the model file:
  [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

* Extract it and place it here:

```
driver-wellness-ai/models/shape_predictor_68_face_landmarks.dat
```

---

## ▶️ Usage

```bash
cd src
python main.py
```

* Webcam will start automatically
* System begins monitoring eye activity
* Press **`q`** to exit

---

## 🛠️ Troubleshooting

**1. dlib installation fails**

* Install Visual Studio Build Tools (Windows)
  → Select *Desktop development with C++*
* Or install a compatible pre-built wheel

**2. Webcam not detected**

* Check if another app is using the camera
* Verify camera permissions

**3. Model file not found**

* Ensure `.dat` file is inside the `models/` folder
* Check file name (no typos)

---

## 📁 Project Structure

```
driver-wellness-ai/
├── models/
│   └── shape_predictor_68_face_landmarks.dat
├── src/
│   ├── main.py
│   ├── face_detector.py
│   └── drowsiness_detector.py
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* 🔊 Add audio alert system
* 📱 Mobile or embedded system integration (Raspberry Pi)
* 🌙 Night-time detection improvements
* 🤖 ML-based fatigue prediction (beyond EAR)
* 📊 Driver analytics dashboard

---

## 📄 License

This project is intended for educational and research purposes.

---
