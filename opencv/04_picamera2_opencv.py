import cv2
import numpy as np
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from libcamera import controls

# Get property
width = 640
height = 480
fps = 15

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('output.mp4',fourcc, fps, (width, height))

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (width, height)}))
picam2.start()

while True:
  ret = picam2.capture_array()
  writer.write(ret)
  cv2.imshow("Capture", ret)
  
  # Close the window if you enter Esc key
  key = cv2.waitKey(1)
  if key == 27:
	  picam2.stop_recording()
	  break

picam2.stop()
writer.release()
cv2.destroyAllWindows()
