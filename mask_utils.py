# mask_utils.py
import cv2
import numpy as np
from config import (
    COLOR_RANGES, MORPH_KERNEL, MORPH_ITERATIONS, DILATE_ITERATIONS,
    CLOAK_TYPE, SMALL_CLOTH_KERNEL, SMALL_CLOTH_MORPH_ITERATIONS, SMALL_CLOTH_DILATE_ITERATIONS
)

def create_mask(frame, color='red'):
    """Create a mask for the cloak color with noise removal and smoothing."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = None
    
    # Create mask for the given color range
    for lower, upper in COLOR_RANGES[color]:
        temp_mask = cv2.inRange(hsv, lower, upper)
        if mask is None:
            mask = temp_mask
        else:
            mask = cv2.add(mask, temp_mask)
    
    # Use parameters based on cloak type
    if CLOAK_TYPE == 'small':
        kernel = np.ones(SMALL_CLOTH_KERNEL, np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=SMALL_CLOTH_MORPH_ITERATIONS)
        mask = cv2.dilate(mask, kernel, iterations=SMALL_CLOTH_DILATE_ITERATIONS)
    else:
        kernel = np.ones(MORPH_KERNEL, np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=MORPH_ITERATIONS)
        mask = cv2.dilate(mask, kernel, iterations=DILATE_ITERATIONS)

    # 🔥 Extra border fix
    # Close small holes and refine edges
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Feather edges to remove harsh white borders
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    return mask
