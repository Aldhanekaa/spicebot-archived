import cv2
import torch
import numpy as np
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Run YOLOv5 model on camera feed and record video on key press.')
parser.add_argument('--model-path', type=str, required=True, help='Path to the custom YOLOv5 model .pt file')
args = parser.parse_args()

# Check if GPU is available
device = "cpu"

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(f"Using device: {device}")

# Load the custom YOLOv5 model on the specified device
model  = torch.hub.load('/Users/aldhan/Documents/dev/yolov5','custom', path=args.model_path,force_reload=True,source='local')

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Initialize video writer (will be set when recording starts)
out = None
recording = False

while True:
    if cap.isOpened:
        ret, frame = cap.read()
        if not ret:
            continue

        # Perform inference on the frame (convert frame to tensor, then to device)
        results = model(frame)

        # Render the results on the frame
        frame = np.squeeze(results.render())

            # Display the frame
        cv2.imshow('YOLOv5 Camera Feed', frame)

    # Check for key press to start/stop recording
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

   

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()