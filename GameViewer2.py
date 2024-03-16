from flask import Flask, Response
import cv2
import torch
import time

app = Flask(__name__)

# Set the device to CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load YOLOv5 model
model_path = r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\david\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\yolov5\runs\train\exp4\weights\best.pt', force_reload=True).to(device)

def gen_frames():  
    cap = cv2.VideoCapture(0)
    prev_frame_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Current time for FPS calculation
        new_frame_time = time.time()
        
        # Convert frame to a compatible tensor format and perform inference
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(frame)

        # Process detection results, calculate centers, and draw bounding boxes
        for *xyxy, conf, cls in results.xyxy[0]:
            x_min, y_min, x_max, y_max = map(int, xyxy)
            x_center = (x_min + x_max) / 2.0
            y_center = (y_min + y_max) / 2.0
            
            # Print the centers as doubles
            print(f'Center: ({x_center:.2f}, {y_center:.2f})')
            
            class_name = model.module.names[int(cls)] if hasattr(model, 'module') else model.names[int(cls)]
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
            cv2.putText(frame, f'{class_name} {conf:.2f}', (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.circle(frame, (int(x_center), int(y_center)), 5, (0, 255, 0), -1)

        # FPS calculation and display on frame
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # Convert back for display
        cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        
        # Encode the frame before sending it to the client
        success, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
