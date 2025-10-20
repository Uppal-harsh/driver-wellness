import cv2
import json
import asyncio
import websockets
from face_detector import FaceDetector
from drowsiness_detector import DrowsinessDetector

async def send_data(websocket, is_drowsy, ear):
    data = {
        "is_drowsy": is_drowsy,
        "ear": ear
    }
    await websocket.send(json.dumps(data))

async def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Initialize detectors
    face_detector = FaceDetector()
    drowsiness_detector = DrowsinessDetector()

    # Connect to WebSocket server
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Detect faces
            faces = face_detector.detect_faces(frame)

            for face in faces:
                landmarks = face_detector.get_facial_landmarks(frame, face)
                is_drowsy, ear = drowsiness_detector.check_drowsiness(landmarks)

                # Send data to server
                await send_data(websocket, is_drowsy, ear)

                # Draw rectangle around face
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if is_drowsy:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("Driver Wellness AI", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
