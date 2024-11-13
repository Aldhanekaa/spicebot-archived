import cv2
import torch
import numpy as np
import argparse

# Check if GPU is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

# print("Initialising cv2")
# Initialize the webcam
cap = cv2.VideoCapture(0)

# print("entering while loop")
# Initialize video writer (will be set when recording starts)
while cap.isOpened():
    # print("read frame")
    ret, frame = cap.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    
    # Display the frame
    cv2.imshow('YOLOv5 Camera Feed', frame)

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()