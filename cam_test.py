import cv2
import time

print("Connecting to webcam...")
cap = cv2.current_cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam connected! Capturing a test frame...")

# Let the camera warm up for a second
time.sleep(1)

# Grab a single frame
ret, frame = cap.read()

if ret:
    # Save the frame to disk so you can verify it saw something
    cv2.imwrite('test_image.jpg', frame)
    print("SUCCESS! Captured a frame and saved it as 'test_image.jpg'")
else:
    print("Error: Could not read frame from webcam.")

cap.release()
