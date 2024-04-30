import numpy as np
import cv2

largeur, hauteur = 320, 320
image = np.ones((hauteur, largeur, 3), dtype=np.uint8) * 255 
epaisseur_bande = 9
l1 = 100
l2 = 109
image[0:100,269:]=(15,185,255)
image[l1:l2,:]=(0,0,0)
image[l1:l2,:]=(0,0,0)
b1=230
b2=239
image[b1:b2, :]=(0,0,0)
v1,v2=50,59
image[:, v1:v2]=(0,0,0)
bd1,bd2=260,269
image[109:230,59:260]=(0,0,255)
image[:,bd1:bd2]=(0,0,0)
image[0:100,269:]=(15,185,255)
image[109:230,59:260]=(0,0,255)
image[239:,59:260]=(255,0,0)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()




cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
