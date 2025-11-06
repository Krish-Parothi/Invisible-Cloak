# background_capture.py
import cv2
import numpy as np

def capture_background(cap, num_frames=60):
    """Capture static background for invisibility effect."""
    print("Capturing background, please stay out of frame...")
    background = None
    for i in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = np.flip(frame, axis=1)
        if background is None:
            background = frame.astype(np.float32)
        else:
            cv2.accumulateWeighted(frame, background, 1.0/(i+1))
    background = cv2.convertScaleAbs(background)
    print("Background captured!")
    return background
