import cv2
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from CNNmodel import CNNModel  

model = CNNModel()

model.load_state_dict(torch.load(r'/home/robo/Downloads/IEEE /CNNmodel.pth'))
model.eval()

def preprocess_frame(frame):
    # Resize the frame to the input size expected by the model
    frame = cv2.resize(frame, (640, 480))

    # Convert BGR image to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to a PyTorch tensor
    transform = transforms.Compose([transforms.ToTensor()])
    frame = transform(frame)

    # Add batch dimension
    frame = frame.unsqueeze(0)

    return frame

cap = cv2.VideoCapture(0)  # 0 for default camera, you can change it if you have multiple cameras

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess the frame
    input_frame = preprocess_frame(frame)

    # Forward pass through the model
    with torch.no_grad():
        output = model(input_frame)

    # Get the predicted class
    _, predicted_class = torch.max(output, 1)
    predicted_class = predicted_class.item()

    # Display the frame with the predicted class
    cv2.putText(frame, f'Detected Class: x', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Object Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


