from flask import Flask, Response
import cv2
import torch
import time

app = Flask(__name__)

class DetectionInfo:
    def __init__(self, class_name, x_center_relative, y_center_relative, confidence):
        self.class_name = class_name
        self.x_center_relative = float(x_center_relative)
        self.y_center_relative = float(y_center_relative)
        self.confidence = float(confidence)

    def __str__(self):
        return f"Class: {self.class_name}, X: {self.x_center_relative:.2f}, Y: {self.y_center_relative:.2f}, Confidence: {self.confidence:.2f}"

# Set the device to CUDA if available, otherwise fall back to CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the trained YOLOv5 model and move it to the chosen device
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt').to(device)

def gen_frames():  
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    
    while True:
        t1 = cv2.getTickCount()
        
        success, frame = cap.read()
        if not success:
            break
        
        # Convert frame to tensor and perform inference
        frame_tensor = torch.from_numpy(frame).permute(2, 0, 1).float().div(255).unsqueeze(0).to(device)
        results = model(frame_tensor)

        # Process detection results
        for *xyxy, conf, cls in results.xyxy[0].tolist():
            x_min, y_min, x_max, y_max = map(int, xyxy)
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2
            frame_width, frame_height = frame.shape[1], frame.shape[0]
            x_center_relative = x_center / frame_width
            y_center_relative = y_center / frame_height
            
            # Create and print DetectionInfo instance
            detection = DetectionInfo(model.names[int(cls)], x_center_relative, y_center_relative, conf)
            print(detection)
            
            # Draw bounding box and class name on the frame
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
            cv2.putText(frame, f'{detection.class_name} {detection.confidence:.2f}', (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        # Calculate and display FPS
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/cv2.getTickFrequency()
        cv2.putText(frame, f'FPS: {1/time1:.2f}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        
        # Encode the processed frame before sending it to the client
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
