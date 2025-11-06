# video_utils.py
import cv2
import os
from config import OUTPUT_DIR, OUTPUT_FILENAME, FRAME_RATE

def initialize_video_writer(frame_shape):
    """Initialize video writer to save output video."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    height, width = frame_shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), fourcc, FRAME_RATE, (width, height))
    return out
