import cv2
import numpy as np

filepath = "data/input.jpg"

img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('output/output.jpg', gray)
