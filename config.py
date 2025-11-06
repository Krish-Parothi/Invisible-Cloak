# config.py
import numpy as np

# Cloak color ranges (HSV)
COLOR_RANGES = {
    "red": [
        (np.array([0, 120, 70]), np.array([10, 255, 255])),
        (np.array([170, 120, 70]), np.array([180, 255, 255]))
    ],
    "blue": [
        (np.array([94, 80, 2]), np.array([126, 255, 255]))
    ],
    "green": [
        (np.array([40, 40, 40]), np.array([70, 255, 255]))
    ],
    "black": [
        (np.array([0, 0, 0]), np.array([180, 255, 50]))  # Low V value for black detection
    ],
    "yellow": [
        (np.array([20, 100, 100]), np.array([35, 255, 255]))
    ],
    "white": [
    (np.array([0, 0, 200]), np.array([180, 30, 255]))
]

}

# Mask processing parameters
MORPH_KERNEL = (3, 3)
MORPH_ITERATIONS = 2
DILATE_ITERATIONS = 1

# Small cloth / rumal parameters
SMALL_CLOTH_KERNEL = (5, 5)
SMALL_CLOTH_MORPH_ITERATIONS = 1
SMALL_CLOTH_DILATE_ITERATIONS = 2

# Choose cloak type
CLOAK_TYPE = 'small'  # 'small' for rumal/scarf, 'full' for full-body cloak

# Video output settings
OUTPUT_DIR = "output/"
OUTPUT_FILENAME = "invisibility_output.avi"
FRAME_RATE = 20.0
