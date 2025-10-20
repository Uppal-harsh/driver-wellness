import cv2
from face_detector import FaceDetector
from drowsiness_detector import DrowsinessDetector

def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Initialize detectors
    face_detector = FaceDetector()
    drowsiness_detector = DrowsinessDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces
        faces = face_detector.detect_faces(frame)

        for face in faces:
            # Get facial landmarks
            landmarks = face_detector.get_facial_landmarks(frame, face)
            
            # Check for drowsiness
            is_drowsy, ear = drowsiness_detector.check_drowsiness(landmarks)

            # Draw rectangle around face
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display drowsiness warning
            if is_drowsy:
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("Driver Wellness AI", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
