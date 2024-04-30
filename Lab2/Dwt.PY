import cv2
import numpy as np
import pywt

def apply_dwt(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coeffs = pywt.dwt2(gray_image, 'haar')
    LL, (LH, HL, HH) = coeffs
    return LL, LH, HL, HH

def apply_idwt(LL, LH, HL, HH):
    reconstructed_image = pywt.idwt2((LL, (LH, HL, HH)), 'haar')
    return reconstructed_image

image = cv2.imread('C:/Users/21620/Desktop/maldives.jpg')
LL, LH, HL, HH = apply_dwt(image)
reconstructed_image = apply_idwt(LL, LH, HL, HH)
cv2.imshow('LL', LL.astype(np.uint8))
cv2.imshow('LH', LH.astype(np.uint8))
cv2.imshow('HL', HL.astype(np.uint8))
cv2.imshow('HH', HH.astype(np.uint8))
cv2.imshow('Reconstructed Image', reconstructed_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
