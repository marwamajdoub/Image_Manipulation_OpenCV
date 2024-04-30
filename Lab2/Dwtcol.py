import cv2
import numpy as np
import pywt

def apply_dwt(image):
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    Y = ycrcb_image[:,:,0]
    coeffs_Y = pywt.dwt2(Y, 'haar')
    LL_Y, (LH_Y, HL_Y, HH_Y) = coeffs_Y
    return LL_Y, LH_Y, HL_Y, HH_Y
def apply_idwt(LL_Y, LH_Y, HL_Y, HH_Y):
    Y_reconstructed = pywt.idwt2((LL_Y, (LH_Y, HL_Y, HH_Y)), 'haar')
    return Y_reconstructed
image = cv2.imread('C:/Users/21620/Desktop/maldives.jpg')
LL_Y, LH_Y, HL_Y, HH_Y = apply_dwt(image)
cv2.imshow('LL_Y', LL_Y.astype(np.uint8))
cv2.imshow('LH_Y', LH_Y.astype(np.uint8))
cv2.imshow('HL_Y', HL_Y.astype(np.uint8))
cv2.imshow('HH_Y', HH_Y.astype(np.uint8))
Y_reconstructed = apply_idwt(LL_Y, LH_Y, HL_Y, HH_Y)
ycrcb_image_reconstructed = np.zeros_like(image, dtype=np.uint8)
ycrcb_image_reconstructed[:,:,0] = Y_reconstructed
ycrcb_image_reconstructed[:,:,1:3] = image[:,:,1:3]  
reconstructed_image = cv2.cvtColor(ycrcb_image_reconstructed, cv2.COLOR_YCrCb2BGR)
cv2.imshow('Reconstructed Image', reconstructed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()