import numpy as np
from scipy.spatial import distance

class DrowsinessDetector:
    def __init__(self, eye_ar_threshold=0.25, eye_ar_consec_frames=48):
        self.eye_ar_threshold = eye_ar_threshold
        self.eye_ar_consec_frames = eye_ar_consec_frames
        self.counter = 0
        self.alarm_on = False

    def eye_aspect_ratio(self, eye):
        # Compute euclidean distances between the vertical eye landmarks
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        # Compute euclidean distance between horizontal eye landmarks
        C = distance.euclidean(eye[0], eye[3])
        # Calculate eye aspect ratio
        ear = (A + B) / (2.0 * C)
        return ear

    def check_drowsiness(self, landmarks):
        # Extract eye coordinates
        left_eye = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                            (landmarks.part(37).x, landmarks.part(37).y),
                            (landmarks.part(38).x, landmarks.part(38).y),
                            (landmarks.part(39).x, landmarks.part(39).y),
                            (landmarks.part(40).x, landmarks.part(40).y),
                            (landmarks.part(41).x, landmarks.part(41).y)])
        
        right_eye = np.array([(landmarks.part(42).x, landmarks.part(42).y),
                             (landmarks.part(43).x, landmarks.part(43).y),
                             (landmarks.part(44).x, landmarks.part(44).y),
                             (landmarks.part(45).x, landmarks.part(45).y),
                             (landmarks.part(46).x, landmarks.part(46).y),
                             (landmarks.part(47).x, landmarks.part(47).y)])

        # Calculate eye aspect ratios
        left_ear = self.eye_aspect_ratio(left_eye)
        right_ear = self.eye_aspect_ratio(right_eye)
        ear = (left_ear + right_ear) / 2.0

        # Check if eyes are closed
        if ear < self.eye_ar_threshold:
            self.counter += 1
            if self.counter >= self.eye_ar_consec_frames:
                self.alarm_on = True
        else:
            self.counter = 0
            self.alarm_on = False

        return self.alarm_on, ear
