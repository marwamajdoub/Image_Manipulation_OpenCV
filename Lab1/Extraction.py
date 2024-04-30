import cv2
import numpy as np 
def extraire_rouge(image):
     rouge_image = np.zeros_like(image)
     rouge_image[:, :, 2] = image[:, :, 2]

     return rouge_image

def extraire_vert(image):

   vert_image = np.zeros_like(image)

   vert_image[:, :, 1] = image[:, :, 1]  

   return vert_image

def extraire_bleu(image):

    bleu_image = np.zeros_like(image)

    bleu_image[:, :, 0] = image[:, :, 0]  

    return bleu_image


image = cv2.imread("C:/Users/21620/Desktop/maldives.jpg")
composante_rouge = extraire_rouge(image)
composante_verte = extraire_vert(image)
composante_bleue = extraire_bleu(image)

cv2.imshow("Composante Rouge", composante_rouge)
cv2.imshow("Composante Verte", composante_verte)
cv2.imshow("Composante Bleue", composante_bleue)


cv2.waitKey(0)
cv2.destroyAllWindows()
