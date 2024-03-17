import cv2
import torch

class BoosterDetector:
    def __init__(self):
        # Load the trained YOLOv5 model
        model_path = r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt'
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.frame_count = 0  # Initialize frame count

    def capture_and_find_boosters_centers(self):
        # Open a connection to the webcam
        cap = cv2.VideoCapture(0)
        
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        
        ret, frame = cap.read()
        if not ret:
            raise IOError("Cannot read from webcam")

        # Increment and save the captured frame with the frame count
        self.frame_count += 1
        save_path = rf'C:\Users\david\OneDrive\Pictures\IEEE pics\Frame{self.frame_count}.jpg'
        cv2.imwrite(save_path, frame)

        # Release the webcam and close any open windows
        cap.release()
        cv2.destroyAllWindows()

        # Make detections
        results = self.model(frame)

        # Get the shape of the frame for normalization
        frame_height, frame_width = frame.shape[:2]

        # Detected objects list with normalized centers
        booster_centers_normalized = []

        # Names of detected classes
        names = results.names

        for *xyxy, conf, cls in results.xyxy[0]:
            x_min, y_min, x_max, y_max = map(int, xyxy)
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2

            # Normalize center coordinates to be relative to the frame
            x_center_normalized = x_center / frame_width
            y_center_normalized = y_center / frame_height

            class_name = names[int(cls)]
        
            if class_name.lower() == 'booster':
                booster_centers_normalized.append((x_center_normalized, y_center_normalized))

        # Sort the list of normalized booster centers by the x-coordinate (leftmost to rightmost)
        booster_centers_normalized.sort(key=lambda x: x[0])

        # Return list of sorted normalized booster centers along with the path of the saved image
        return booster_centers_normalized, save_path

# Example usage
if __name__ == "__main__":
    detector = BoosterDetector()
    for _ in range(5):  # Example loop, adjust as necessary
        centers_normalized, image_path = detector.capture_and_find_boosters_centers()
        print("Normalized booster centers:", centers_normalized)
        print(f"Image saved to {image_path}")
