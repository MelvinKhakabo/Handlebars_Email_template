# Edit Iki_logo to black
#import cv2
#import numpy as np

#image = cv2.imread("Iki_logo.png", cv2.IMREAD_GRAYSCALE)
#inverted = cv2.bitwise_not(image)
#cv2.imwrite("black_Iki_logo.png", inverted)

# Remove the background color of the image
import cv2
import numpy as np

# Load the image
image = cv2.imread("black_Iki_logo.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to separate background
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Create mask where white is background
mask = cv2.bitwise_not(thresh)

# Convert to 3 channels (for color images)
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# Remove background by applying mask
result = cv2.bitwise_and(image, mask)

# Save the result
cv2.imwrite("Iki_no_background.png", result)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


