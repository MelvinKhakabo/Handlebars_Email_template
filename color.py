import cv2
import numpy as np

image = cv2.imread("Iki_logo.png", cv2.IMREAD_GRAYSCALE)
inverted = cv2.bitwise_not(image)
cv2.imwrite("black_Iki_logo.png", inverted)
