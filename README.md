# Driver Wellness AI

Driver Wellness AI is a Python-based real-time drowsiness detection system using computer vision and facial landmark analysis. It monitors a driver's eye aspect ratio via webcam and alerts when signs of drowsiness are detected.

## Features

- Real-time face and eye detection using OpenCV and dlib
- Drowsiness detection based on eye aspect ratio (EAR)
- Visual alert overlay when drowsiness is detected

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd driver-wellness-ai
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Facial Landmark Model

- Download [shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- Extract the `.dat` file and place it in the `models` directory:
  ```
  driver-wellness-ai/models/shape_predictor_68_face_landmarks.dat
  ```

## Usage

```bash
cd src
python main.py
```

- The webcam window will open and start monitoring.
- Press `q` to quit.

## Troubleshooting

- **dlib installation fails:**  
  - Install Visual Studio Build Tools (Windows) with "Desktop development with C++".
  - Alternatively, use a pre-built dlib wheel matching your Python version.
- **Webcam not detected:**  
  - Ensure your webcam is connected and accessible.
- **Model file not found:**  
  - Confirm `shape_predictor_68_face_landmarks.dat` is in the `models` directory.

## Project Structure

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

## License

This project is for educational purposes.
