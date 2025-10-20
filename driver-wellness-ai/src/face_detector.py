import dlib
import cv2
import numpy as np
import os

class FaceDetector:
    def __init__(self):
        # Initialize face detector from dlib
        self.detector = dlib.get_frontal_face_detector()
        # Get the path to the shape predictor file
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                 "models", 
                                 "shape_predictor_68_face_landmarks.dat")
        # Initialize facial landmarks predictor
        self.predictor = dlib.shape_predictor(model_path)

    def detect_faces(self, frame):
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = self.detector(gray)
        return faces

    def get_facial_landmarks(self, frame, face):
        # Get facial landmarks
        landmarks = self.predictor(frame, face)
        return landmarks
