import cv2
import torch
import numpy as np

# Load the trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt')

# Open a connection to the webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

class ObjectDetector:
    def __init__(self):
        # Load the trained YOLOv5 model
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt')

    def get_detections(self, frame):
        # Make detections
        results = self.model(frame)

        # Get the shape of the frame for normalization
        frame_height, frame_width = frame.shape[:2]

        # Detected objects list
        detected_objects = []

        # Names of detected classes
        names = results.names

        for *xyxy, conf, cls in results.xyxy[0]:
            x_min, y_min, x_max, y_max = map(int, xyxy)
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2

            # Normalize center coordinates to be relative to the frame
            x_center_relative = x_center / frame_width
            y_center_relative = y_center / frame_height

            class_name = names[int(cls)]
            detected_objects.append((class_name, x_center_relative, y_center_relative))

        return detected_objects

    def run(self):
        # Open a connection to the webcam
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            detections = self.get_detections(frame)

            for class_name, x_center_relative, y_center_relative in detections:
                # Convert relative positions back to actual positions for visualization
                x_center = int(x_center_relative * frame.shape[1])
                y_center = int(y_center_relative * frame.shape[0])

                # For demonstration, use a placeholder for bounding box coordinates
                x_min, y_min, x_max, y_max = x_center - 50, y_center - 50, x_center + 50, y_center + 50

                # Draw rectangle (bounding box) and circle (center)
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
                cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), -1)

                # Show class name and normalized coordinates
                text = f'{class_name} ({x_center_relative:.2f}, {y_center_relative:.2f})'
                cv2.putText(frame, text, (x_center, y_center - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Display the frame
            cv2.imshow('YOLOv5 Webcam', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the webcam and close the window
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = ObjectDetector()
    detector.run()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Make detections
    results = model(frame)

    # Get the shape of the frame
    frame_height, frame_width = frame.shape[:2]

    # Names of detected classes
    names = results.names

    # Draw bounding boxes, centers, and class names on the frame
    for *xyxy, conf, cls in results.xyxy[0]:
        # Extract xy coordinates
        x_min, y_min, x_max, y_max = map(int, xyxy)

        # Calculate center
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        # Normalize center coordinates to be relative to the frame
        x_center_relative = x_center / frame_width
        y_center_relative = y_center / frame_height

        # Get the class name
        class_name = names[int(cls)]

        # Draw rectangle (bounding box)
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)

        # Draw circle (center)
        cv2.circle(frame, (int(x_center), int(y_center)), 5, (0, 255, 0), -1)

        # Show normalized coordinates and class name
        text = f'{class_name} ({x_center_relative:.2f}, {y_center_relative:.2f})'
        cv2.putText(frame, text, (int(x_center), int(y_center) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow('YOLOv5 Webcam', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
