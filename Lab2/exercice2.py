import cv2
import numpy as np
def apply_dct(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image_float32 = np.float32(gray_image)/255.0
    dct_image = cv2.dct(gray_image_float32)
    return dct_image

def apply_idct(dct_image):
    idct_image = cv2.idct(dct_image)
    return idct_image
def apply_dct_color(image):
    b, g, r = cv2.split(image)
    dct_b = cv2.dct(np.float32(b))
    dct_g = cv2.dct(np.float32(g))
    dct_r = cv2.dct(np.float32(r))
    return dct_b, dct_g, dct_r

def apply_idct_color(dct_b, dct_g, dct_r):
    idct_b = cv2.idct(dct_b)
    idct_g = cv2.idct(dct_g)
    idct_r = cv2.idct(dct_r)
    reconstructed_image = cv2.merge((idct_b, idct_g, idct_r))
    return reconstructed_image

image = cv2.imread('C:/Users/21620/Desktop/maldives.jpg')
dct_b, dct_g, dct_r = apply_dct_color(image)
reconstructed_image = apply_idct_color(dct_b, dct_g, dct_r)
cv2.imshow('Original Image', image)
cv2.imshow('Reconstructed Image', reconstructed_image.astype(np.uint8))
cv2.imshow('Original Image', image)
dct_result = apply_dct(image)
idct_result = apply_idct(dct_result)
LL, LH, HL, HH = apply_dwt(image)
cv2.imshow('DCT Image', dct_result)
cv2.imshow('IDCT Image', idct_result)
cv2.imshow('LL, LH, HL, HH ', idct_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

