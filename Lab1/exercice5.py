import cv2

def invert_colors(image):
    inverted_image = 255 - image
    return inverted_image
image = cv2.imread("C:/Users/21620/Desktop/maldives.jpg")
inverted_image = invert_colors(image)
cv2.imshow("Image inversée", inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
