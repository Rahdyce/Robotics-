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

# Load the trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt')

def gen_frames():  
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    
    # Initialize frame rate calculation
    freq = cv2.getTickFrequency()
    
    while True:
        t1 = cv2.getTickCount()
        
        success, frame = cap.read()
        if not success:
            break
        
        # Get the shape of the frame
        frame_height, frame_width = frame.shape[:2]

        # Make detections
        results = model(frame)

        # Process detection results and create DetectionInfo instances
        detections = []
        for *xyxy, conf, cls in results.xyxy[0]:
            x_min, y_min, x_max, y_max = map(int, xyxy)
            x_center = (x_min + x_max) / 2
            y_center = (y_min + y_max) / 2
            x_center_relative = x_center / frame_width
            y_center_relative = y_center / frame_height
            detection = DetectionInfo(results.names[int(cls)], x_center_relative, y_center_relative, conf)
            detections.append(detection)

            # Optionally, for debugging or monitoring, print detection info
            print(detection)
        
        # Calculate and display FPS
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        frame_rate_calc = 1/time1
        cv2.putText(frame,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
        
        # Encode the processed frame before sending it to the client
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
