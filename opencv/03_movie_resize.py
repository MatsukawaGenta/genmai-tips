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

# Resize
resize_w = 640
resize_h = 480

# Show property
print("WIDTH:", width)
print("HEIGHT:", height)
print("FPS:", fps)
print("FRAME NUM:", frame_num)
print("Play TIME[sec]:", play_time)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('output/resize.mp4',fourcc, fps, (resize_w, resize_h))

# Loop until end of movie
while(cap.isOpened()):
    # Get frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (resize_w, resize_h))
        writer.write(frame)  
    else:
        break

cap.release()
writer.release()