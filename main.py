import cv2
import numpy as np
from mask_utils import create_mask
from background_capture import capture_background
from video_utils import initialize_video_writer

# Fixed display size (Full HD)
WIDTH, HEIGHT = 1920, 1080

def resize_with_padding(frame, target_size=(WIDTH, HEIGHT)):
    """Resize frame to fit inside target size while keeping aspect ratio, add black padding."""
    h, w = frame.shape[:2]
    target_w, target_h = target_size

    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)

    resized = cv2.resize(frame, (new_w, new_h))

    # Create black canvas and paste resized frame in the center
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    canvas[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized

    return canvas

def invisibility_cloak(video_source=0, cloak_color='blue', save_output=True):
    cap = cv2.VideoCapture(video_source)
    
    # Capture background first
    background = capture_background(cap)
    background = resize_with_padding(background, (WIDTH, HEIGHT))
    
    # Initialize video writer with fixed 1920x1080
    out = initialize_video_writer((HEIGHT, WIDTH, 3)) if save_output else None

    print("Hold the rumal/cloth in front of you to become invisible!")
    print("Press 'q' to quit the program.")
    
    # Setup window
    cv2.namedWindow("Invisibility Cloak (Rumal Mode)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Invisibility Cloak (Rumal Mode)", WIDTH, HEIGHT)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)  # Mirror frame
        frame = resize_with_padding(frame, (WIDTH, HEIGHT))  # Keep aspect ratio
        
        # Create mask for cloak color
        mask = create_mask(frame, cloak_color)
        mask_inv = cv2.bitwise_not(mask)
        
        # Combine background and current frame
        part1 = cv2.bitwise_and(background, background, mask=mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final_output = cv2.addWeighted(part1, 1, part2, 1, 0)
        
        # Show live invisibility effect
        cv2.imshow("Invisibility Cloak (Rumal Mode)", final_output)
        
        # Save output video
        if save_output:
            out.write(final_output)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if save_output:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    invisibility_cloak(video_source=0, cloak_color='blue', save_output=True)
