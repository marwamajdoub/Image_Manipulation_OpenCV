import cv2
import numpy as np

def convert_to_grayscale(image):
    gray_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return gray_image

image = cv2.imread('C:/Users/21620/Desktop/maldives.jpg')
gray_image = convert_to_grayscale(image)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
