import cv2
import numpy as np

filepath = "data/input.mp4"

# input movie
cap = cv2.VideoCapture(filepath)

# Get property
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
play_time = frame_num / fps

# Show property
print("WIDTH:", width)
print("HEIGHT:", height)
print("FPS:", fps)
print("FRAME NUM:", frame_num)
print("Play TIME[sec]:", play_time)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('output/output.mp4',fourcc, fps, (width, height))

# Loop until end of movie
while(cap.isOpened()):
    # Get frame
    ret, frame = cap.read()
    if ret == True:
        # write the flipped frame
        frame = cv2.flip(frame,0)
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Convert to 3ch for saved movie
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        # Draw rectangle
        cv2.rectangle(gray, (10, 20), (100, 100), color=(0,0,255),thickness= 4)
        writer.write(gray)  
    else:
        break

cap.release()
writer.release()