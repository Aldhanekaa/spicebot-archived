# add option of OS ; macOS and linux

import cv2
import torch
import numpy as np
import argparse

torch.set_warn_always(False)

device = "cpu"

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(f"Using device: {device}")

print("Load Parser")

# Set up argument parser
parser = argparse.ArgumentParser(description='Run YOLOv5 model on camera feed and record video on key press.')
parser.add_argument('--model-path', type=str, required=True, help='Path to the custom YOLOv5 model .pt file')
args = parser.parse_args()

print("Load Model")
# Load the custom YOLOv5 model
model  = torch.hub.load('/Users/aldhan/Documents/dev/yolov5','custom', path=args.model_path,force_reload=True,source='local')

print("Load CV2")

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Initialize video writer (will be set when recording starts)
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Codec for .avi format
out = None
recording = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Perform inference on the frame
    results = model(frame)

    # Render the results on the frame
    frame = np.squeeze(results.render())

    # Check for key press to start/stop recording
    key = cv2.waitKey(1) & 0xFF
    print(f"PRESSED ! {key}")
    if key == ord('r'):
        if not recording:
            # Start recording
            out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            recording = True
            print("Recording started...!!!")
        else:
            # Stop recording
            recording = False
            out.release()
            print("Recording stopped and saved as 'output.avi'")
    elif key == ord('q'):
        break

    # Write the frame to the video file if recording
    if recording:
        out.write(frame)

    # Display the frame
    cv2.imshow('YOLOv5 Camera Feed', frame)

# Release the webcam and close the window
cap.release()
if out:
    out.release()
cv2.destroyAllWindows()